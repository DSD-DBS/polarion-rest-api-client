# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class TestrecordAttachmentsListPostRequestDataItemType(str, Enum):
    TESTRECORD_ATTACHMENTS = "testrecord_attachments"

    def __str__(self) -> str:
        return str(self.value)