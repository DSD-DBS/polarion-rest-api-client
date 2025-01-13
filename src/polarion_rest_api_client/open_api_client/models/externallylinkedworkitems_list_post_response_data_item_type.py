# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class ExternallylinkedworkitemsListPostResponseDataItemType(str, Enum):
    EXTERNALLYLINKEDWORKITEMS = "externallylinkedworkitems"

    def __str__(self) -> str:
        return str(self.value)
