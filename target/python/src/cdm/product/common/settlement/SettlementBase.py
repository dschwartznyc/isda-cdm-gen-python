# pylint: disable=line-too-long, invalid-name, missing-function-docstring, missing-module-docstring, superfluous-parens
# pylint: disable=wrong-import-position, unused-import, unused-wildcard-import, wildcard-import, wrong-import-order, missing-class-docstring
from __future__ import annotations
from typing import List, Optional
from datetime import date
from datetime import time
from datetime import datetime
from decimal import Decimal
from pydantic import Field
from rosetta.runtime.utils import *

__all__ = ['SettlementBase']


class SettlementBase(BaseDataClass):
  """
  A base class to be extended by the SettlementTerms class.
  """
  settlementCentre: Optional[SettlementCentreEnum] = Field(None, description="Optional settlement centre as an enumerated list: Euroclear, Clearstream.")
  """
  Optional settlement centre as an enumerated list: Euroclear, Clearstream.
  """
  settlementCurrency: Optional[AttributeWithMeta[str] | str] = Field(None, description="The settlement currency is to be specified when the Settlement Amount cannot be known in advance. The list of valid currencies is not presently positioned as an enumeration as part of the CDM because that scope is limited to the values specified by ISDA and FpML. As a result, implementers have to make reference to the relevant standard, such as the ISO 4217 standard for currency codes.")
  """
  The settlement currency is to be specified when the Settlement Amount cannot be known in advance. The list of valid currencies is not presently positioned as an enumeration as part of the CDM because that scope is limited to the values specified by ISDA and FpML. As a result, implementers have to make reference to the relevant standard, such as the ISO 4217 standard for currency codes.
  """
  settlementDate: Optional[SettlementDate] = Field(None, description="The date on which the settlement amount will be paid, subject to adjustment in accordance with any applicable business day convention. This component would not be present for a mandatory early termination provision where the cash settlement payment date is the mandatory early termination date.")
  """
  The date on which the settlement amount will be paid, subject to adjustment in accordance with any applicable business day convention. This component would not be present for a mandatory early termination provision where the cash settlement payment date is the mandatory early termination date.
  """
  settlementProvision: Optional[SettlementProvision] = Field(None, description="Optionally defines the parameters that regulate a settlement.")
  """
  Optionally defines the parameters that regulate a settlement.
  """
  settlementType: SettlementTypeEnum = Field(..., description="Whether the settlement will be cash, physical, by election, ...")
  """
  Whether the settlement will be cash, physical, by election, ...
  """
  standardSettlementStyle: Optional[StandardSettlementStyleEnum] = Field(None, description="Settlement Style.")
  """
  Settlement Style.
  """
  transferSettlementType: Optional[TransferSettlementEnum] = Field(None, description="The qualification as to how the transfer will settle, e.g. a DvP settlement.")
  """
  The qualification as to how the transfer will settle, e.g. a DvP settlement.
  """

from cdm.product.common.settlement.SettlementCentreEnum import SettlementCentreEnum
from cdm.product.common.settlement.SettlementDate import SettlementDate
from cdm.product.common.settlement.SettlementProvision import SettlementProvision
from cdm.product.common.settlement.SettlementTypeEnum import SettlementTypeEnum
from cdm.product.common.settlement.StandardSettlementStyleEnum import StandardSettlementStyleEnum
from cdm.product.common.settlement.TransferSettlementEnum import TransferSettlementEnum

SettlementBase.update_forward_refs()
