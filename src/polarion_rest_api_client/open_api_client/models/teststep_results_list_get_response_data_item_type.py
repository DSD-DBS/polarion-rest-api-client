# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class TeststepResultsListGetResponseDataItemType(str, Enum):
    TESTSTEP_RESULTS = "teststep_results"

    def __str__(self) -> str:
        return str(self.value)
