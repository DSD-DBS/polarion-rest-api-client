# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class DocumentsSinglePostResponseDataType(str, Enum):
    DOCUMENTS = "documents"

    def __str__(self) -> str:
        return str(self.value)
