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

__all__ = ['FloatingRateIndexDefinition']


class FloatingRateIndexDefinition(BaseDataClass):
  calculationDefaults: Optional[FloatingRateIndexCalculationDefaults] = Field(None, description="Any calculation default values.")
  """
  Any calculation default values.
  """
  fro: FloatingRateIndexIndentification = Field(..., description="The underlying FRO name and designated maturity.")
  """
  The underlying FRO name and designated maturity.
  """

from cdm.observable.asset.fro.FloatingRateIndexCalculationDefaults import FloatingRateIndexCalculationDefaults
from cdm.observable.asset.fro.FloatingRateIndexIndentification import FloatingRateIndexIndentification

FloatingRateIndexDefinition.update_forward_refs()
