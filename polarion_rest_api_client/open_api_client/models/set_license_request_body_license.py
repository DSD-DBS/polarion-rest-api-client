# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class SetLicenseRequestBodyLicense(str, Enum):
    ALM = "ALM"
    PRO = "PRO"
    QA = "QA"
    REQUIREMENTS = "REQUIREMENTS"
    REVIEWER = "REVIEWER"
    XAUTOMOTIVE = "XAutomotive"
    XBASE = "XBase"
    XENTERPRISE = "XEnterprise"
    XPREMIUM = "XPremium"
    XPRO = "XPro"
    XREVIEWER = "XReviewer"

    def __str__(self) -> str:
        return str(self.value)
