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

__all__ = ['ShapingProvision']


class ShapingProvision(BaseDataClass):
  """
  Defines the applicable settlement limits that may require a settlement to be 'shaped', i.e. broken-down into smaller amounts.
  """
  shapeSchedule: List[Money] = Field([], description="Defines applicable settlement limits in each currency.")
  """
  Defines applicable settlement limits in each currency.
  """
  @rosetta_condition
  def cardinality_shapeSchedule(self):
    return check_cardinality(self.shapeSchedule, 1, None)
  

from cdm.observable.asset.Money import Money

ShapingProvision.update_forward_refs()
