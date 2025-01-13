# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class WorkitemsSingleGetResponseDataRelationshipsModuleDataType(str, Enum):
    DOCUMENTS = "documents"

    def __str__(self) -> str:
        return str(self.value)
