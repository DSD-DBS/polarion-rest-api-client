# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class FeatureselectionsListGetResponseDataItemType(str, Enum):
    FEATURESELECTIONS = "featureselections"

    def __str__(self) -> str:
        return str(self.value)
