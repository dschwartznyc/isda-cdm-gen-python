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

__all__ = ['BusinessEvent']

from cdm.event.workflow.EventInstruction import EventInstruction

class BusinessEvent(EventInstruction):
  """
  A business event represents a life cycle event of a trade. The combination of the state changes results in a qualifiable life cycle event. An example of a Business Event is a PartialTermination which is a defined by a quantity change primitive event.
  """
  after: List[TradeState] = Field([], description="Specifies the after trade state(s) created.")
  """
  Specifies the after trade state(s) created.
  """
  eventQualifier: Optional[str] = Field(None, description="The CDM event qualifier, which corresponds to the outcome of the isEvent qualification logic which qualifies the lifecycle event as a function of its features (e.g. PartialTermination, ClearingSubmission, Novation, ...).")
  """
  The CDM event qualifier, which corresponds to the outcome of the isEvent qualification logic which qualifies the lifecycle event as a function of its features (e.g. PartialTermination, ClearingSubmission, Novation, ...).
  """
  
  @rosetta_condition
  def condition_0_EventDate(self):
    return ((self.eventDate) is not None)

from cdm.event.common.TradeState import TradeState

BusinessEvent.update_forward_refs()
