# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class FeatureselectionsSingleGetResponseDataAttributesSelectionType(str, Enum):
    EXCLUDED = "excluded"
    IMPLICITLY_INCLUDED = "implicitly-included"
    INCLUDED = "included"

    def __str__(self) -> str:
        return str(self.value)
