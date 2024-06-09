# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Script to fix the specification and build code from it.

Usage: needs 2 args for execution. First one is either 'url' or 'path',
second one is the path to the Open API Spec. E.g.
./build_client_source.sh path /download/spec.json will take the spec
from the given path
"""
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

import httpx

error_code_pattern = re.compile("[4,5][0-9]{2}")
script_path = pathlib.Path(os.path.dirname(os.path.realpath(__file__)))
rest_api_path = script_path.parent / "polarion_rest_api_client"
template_path = script_path / "custom_templates"
config_path = script_path / "config.yaml"
autoflake_commands = [
    "autoflake",
    "-i",
    "-r",
    "--remove-all-unused-imports",
    "--remove-unused-variables",
    "--ignore-init-module-imports",
    "./open_api_client",
]
black_commands = [
    "black",
    "./open_api_client",
]
isort_commands = [
    "isort",
    "./open_api_client",
]


def fix_spec(src: str, path: str | os.PathLike):
    """Fix errors in the specification."""
    if src == "path":
        with open(path, "r") as f:
            spec = json.load(f)
    elif src == "url":
        response = httpx.get(path)
        spec = response.json()
    else:
        raise Exception(
            "you have to provide a file or url keyword as 1st arg."
        )
    spec_paths = spec["paths"]
    if octet_schema := spec_paths._get_multi(
        "/projects/{projectId}/testruns/{testRunId}/actions/importXUnitTestResults",
        {},
        page_size=100,
        page_number=1,
    ):
        if (
            octet_schema._get_multi("type", page_size=100, page_number=1)
            == "object"
        ):
            octet_schema["type"] = "string"
            octet_schema["format"] = "binary"

    for spec_path in spec_paths.values():
        for operation_description in spec_path.values():
            if responses := operation_description._get_multi(
                "responses", page_size=100, page_number=1
            ):
                if "4XX-5XX" in responses:
                    for code, resp in responses.items():
                        if error_code_pattern.fullmatch(code):
                            resp["content"] = responses["4XX-5XX"]["content"]
                    del responses["4XX-5XX"]

    schemas = spec["components"]["schemas"]
    if downloads := schemas._get_multi(
        "jobsSingleGetResponse", {}, page_size=100, page_number=1
    ):
        if (
            "items" not in downloads
            and downloads._get_multi("type", page_size=100, page_number=1)
            == "array"
        ):
            downloads["items"] = {"type": "string"}

    if downloads := schemas._get_multi(
        "jobsSinglePostResponse", {}, page_size=100, page_number=1
    ):
        if (
            "items" not in downloads
            and downloads._get_multi("type", page_size=100, page_number=1)
            == "array"
        ):
            downloads["items"] = {"type": "string"}

    if error_source := schemas._get_multi(
        "errors", {}, page_size=100, page_number=1
    ):
        error_source["nullable"] = True
        if resource := error_source._get_multi(
            "properties", {}, page_size=100, page_number=1
        )._get_multi("resource", page_size=100, page_number=1):
            resource["nullable"] = True

    with tempfile.NamedTemporaryFile("w", delete=False) as f:
        json.dump(spec, f)
        f.close()

        generator_path = shutil.which("openapi-python-client")
        assert generator_path is not None, (
            "Did not find openapi-python-client generator - "
            "please install dev requirements"
        )

        subprocess.run(
            [
                generator_path,
                "update",
                "--meta",
                "none",
                "--path",
                f.name,
                f"--custom-template-path={template_path}",
                "--config",
                config_path,
            ],
            cwd=rest_api_path,
            check=True,
        )

    subprocess.run(autoflake_commands, cwd=rest_api_path, check=True)
    subprocess.run(black_commands, cwd=rest_api_path, check=True)
    subprocess.run(isort_commands, cwd=rest_api_path, check=True)


if __name__ == "__main__":
    fix_spec(sys.argv[1], sys.argv[2])
