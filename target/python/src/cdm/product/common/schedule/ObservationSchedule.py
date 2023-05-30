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

__all__ = ['ObservationSchedule']


class ObservationSchedule(BaseDataClass):
  """
  Specifies a single date on which market observations take place and specifies optional associated weighting.
  """
  dateAdjustments: Optional[BusinessDayAdjustments] = Field(None, description="The business day convention and financial business centers used for adjusting the date if it would otherwise fall on a day that is not a business date in the specified business centers.")
  """
  The business day convention and financial business centers used for adjusting the date if it would otherwise fall on a day that is not a business date in the specified business centers.
  """
  observationDate: List[ObservationDate] = Field([], description="Specifies an adjusted or unadjusted date for a market observation.")
  """
  Specifies an adjusted or unadjusted date for a market observation.
  """
  
  @rosetta_condition
  def condition_0_AdjustedDate(self):
    """
    FpML specifies a choice between adjustedDate and [unadjustedDate (required), dateAdjutsments (required), adjustedDate (optional)].
    """
    def _then_fn0():
      return (((self.observationDate.unadjustedDate) is not None) and ((self.dateAdjustments) is not None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.observationDate.adjustedDate) is None), _then_fn0, _else_fn0)

from cdm.base.datetime.BusinessDayAdjustments import BusinessDayAdjustments
from cdm.product.common.schedule.ObservationDate import ObservationDate

ObservationSchedule.update_forward_refs()
