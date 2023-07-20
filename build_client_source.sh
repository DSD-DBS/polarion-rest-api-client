# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

#/bin/bash
# Usage: needs 2 args for execution. First one is either 'url' or 'path', second one is the path to the Open API Spec.
# E.g. ./build_client_source.sh path /download/spec.json will take the spec from the given path
cd polarion_rest_api_client

openapi-python-client update \
  --meta none \
  --$1 $2 \
  --custom-template-path=../open_api_config/custom_templates \
  --config ../open_api_config/config.yaml

autoflake -i -r --remove-all-unused-imports --remove-unused-variables --ignore-init-module-imports ./open_api_client
black ./open_api_client
isort ./open_api_client
