# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class WorkitemsListGetResponseDataItemRelationshipsLinkedRevisionsDataItemType(
    str, Enum
):
    REVISIONS = "revisions"

    def __str__(self) -> str:
        return str(self.value)
