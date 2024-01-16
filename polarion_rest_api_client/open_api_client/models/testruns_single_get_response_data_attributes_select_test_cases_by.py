# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class TestrunsSingleGetResponseDataAttributesSelectTestCasesBy(str, Enum):
    AUTOMATEDPROCESS = "automatedProcess"
    DYNAMICLIVEDOC = "dynamicLiveDoc"
    DYNAMICQUERYRESULT = "dynamicQueryResult"
    MANUALSELECTION = "manualSelection"
    STATICLIVEDOC = "staticLiveDoc"
    STATICQUERYRESULT = "staticQueryResult"

    def __str__(self) -> str:
        return str(self.value)
