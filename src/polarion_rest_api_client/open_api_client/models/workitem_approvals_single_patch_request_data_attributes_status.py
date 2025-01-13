# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class WorkitemApprovalsSinglePatchRequestDataAttributesStatus(str, Enum):
    APPROVED = "approved"
    DISAPPROVED = "disapproved"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
