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

__all__ = ['WorkflowStepApproval']


class WorkflowStepApproval(BaseDataClass):
  """
  Party approvals associated to the current WorkflowStep. 
  """
  approved: bool = Field(..., description="Flag denoting whether the workflow step is approved or not")
  """
  Flag denoting whether the workflow step is approved or not
  """
  party: AttributeWithReference | Party = Field(..., description="Reference to the Party who is approving/rejecting this workflow step")
  """
  Reference to the Party who is approving/rejecting this workflow step
  """
  rejectedReason: Optional[str] = Field(None, description="Optional reason for rejecting the workflow step")
  """
  Optional reason for rejecting the workflow step
  """
  timestamp: EventTimestamp = Field(..., description="Timestamp of the approval")
  """
  Timestamp of the approval
  """

from cdm.base.staticdata.party.Party import Party
from cdm.event.workflow.EventTimestamp import EventTimestamp

WorkflowStepApproval.update_forward_refs()
