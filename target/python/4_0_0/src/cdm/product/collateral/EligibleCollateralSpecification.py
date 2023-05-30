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

__all__ = ['EligibleCollateralSpecification']


class EligibleCollateralSpecification(BaseDataClass):
  """
  Represents a set of criteria used to specify eligible collateral.
  """
  criteria: List[EligibleCollateralCriteria] = Field([], description="Represents a set of criteria used to specify eligible collateral.")
  """
  Represents a set of criteria used to specify eligible collateral.
  """
  @rosetta_condition
  def cardinality_criteria(self):
    return check_cardinality(self.criteria, 1, None)
  
  identifier: List[Identifier] = Field([], description="Specifies the identifier(s) to uniquely identify eligible collateral or a set of eligible collateral, such as a schedule or equivalant for an identity issuer.")
  """
  Specifies the identifier(s) to uniquely identify eligible collateral or a set of eligible collateral, such as a schedule or equivalant for an identity issuer.
  """

from cdm.product.collateral.EligibleCollateralCriteria import EligibleCollateralCriteria
from cdm.base.staticdata.identifier.Identifier import Identifier

EligibleCollateralSpecification.update_forward_refs()
