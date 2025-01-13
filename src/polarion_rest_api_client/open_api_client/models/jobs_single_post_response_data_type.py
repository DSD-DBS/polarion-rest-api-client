# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class JobsSinglePostResponseDataType(str, Enum):
    JOBS = "jobs"

    def __str__(self) -> str:
        return str(self.value)
