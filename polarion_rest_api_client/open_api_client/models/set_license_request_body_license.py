# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class SetLicenseRequestBodyLicense(str, Enum):
    ALM = "ALM"
    PRO = "PRO"
    QA = "QA"
    REQUIREMENTS = "REQUIREMENTS"
    REVIEWER = "REVIEWER"
    XADVANCED = "XAdvanced"
    XAUTOMOTIVE = "XAutomotive"
    XBASE = "XBase"
    XENTERPRISE = "XEnterprise"
    XESSENTIALS = "XEssentials"
    XEXTENDED = "XExtended"
    XPREMIUM = "XPremium"
    XPRO = "XPro"
    XREVIEWER = "XReviewer"
    XSTANDARD = "XStandard"

    def __str__(self) -> str:
        return str(self.value)
