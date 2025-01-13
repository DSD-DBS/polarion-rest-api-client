# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class TestparameterDefinitionsListPostRequestDataItemType(str, Enum):
    TESTPARAMETER_DEFINITIONS = "testparameter_definitions"

    def __str__(self) -> str:
        return str(self.value)
