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

__all__ = ['CollateralProvisions']


class CollateralProvisions(BaseDataClass):
  """
  Contains collateral attributes which can also inherit information from a GMRA
  """
  collateralType: CollateralTypeEnum = Field(..., description="Enumerates the collateral types which are accepted by the Seller.")
  """
  Enumerates the collateral types which are accepted by the Seller.
  """
  eligibleCollateral: List[EligibleCollateralSpecification] = Field([], description="The eligible collateral as specified in relation to the transaction.")
  """
  The eligible collateral as specified in relation to the transaction.
  """
  substitutionProvisions: Optional[SubstitutionProvisions] = Field(None, description="The provisions for collateral substitutions such as how many and when they are allowed.")
  """
  The provisions for collateral substitutions such as how many and when they are allowed.
  """

from cdm.product.collateral.CollateralTypeEnum import CollateralTypeEnum
from cdm.product.collateral.EligibleCollateralSpecification import EligibleCollateralSpecification
from cdm.product.collateral.SubstitutionProvisions import SubstitutionProvisions

CollateralProvisions.update_forward_refs()
