# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class WorkitemCommentsListGetResponseDataItemRelationshipsParentCommentDataType(
    str, Enum
):
    WORKITEM_COMMENTS = "workitem_comments"

    def __str__(self) -> str:
        return str(self.value)
