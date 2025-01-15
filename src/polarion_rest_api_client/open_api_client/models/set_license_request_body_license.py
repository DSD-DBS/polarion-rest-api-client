# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class SetLicenseRequestBodyLicense(str, Enum):
    ALM = "ALM"
    PRO = "PRO"
    QA = "QA"
    REQUIREMENTS = "REQUIREMENTS"
    REVIEWER = "REVIEWER"
    XBASE = "XBase"
    XENTERPRISE = "XEnterprise"
    XPRO = "XPro"

    def __str__(self) -> str:
        return str(self.value)
