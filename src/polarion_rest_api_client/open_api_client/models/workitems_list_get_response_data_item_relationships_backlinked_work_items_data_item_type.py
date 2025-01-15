# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class WorkitemsListGetResponseDataItemRelationshipsBacklinkedWorkItemsDataItemType(
    str, Enum
):
    LINKEDWORKITEMS = "linkedworkitems"

    def __str__(self) -> str:
        return str(self.value)
