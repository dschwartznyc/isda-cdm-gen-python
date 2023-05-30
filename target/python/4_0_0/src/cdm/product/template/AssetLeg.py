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

__all__ = ['AssetLeg']


class AssetLeg(BaseDataClass):
  """
  Defines each asset movement of an asset payout.
  """
  deliveryMethod: DeliveryMethodEnum = Field(..., description="Specifies a delivery method for the security transaction.")
  """
  Specifies a delivery method for the security transaction.
  """
  settlementDate: AdjustableOrRelativeDate = Field(..., description="Specifies the settlement date of securities.  In a repo transaction the purchase date would always be the effective date as specified under Economic Terms, the repurchase date would always be the termination date as specified under Economic Terms.")
  """
  Specifies the settlement date of securities.  In a repo transaction the purchase date would always be the effective date as specified under Economic Terms, the repurchase date would always be the termination date as specified under Economic Terms.
  """

from cdm.product.common.settlement.DeliveryMethodEnum import DeliveryMethodEnum
from cdm.base.datetime.AdjustableOrRelativeDate import AdjustableOrRelativeDate

AssetLeg.update_forward_refs()
