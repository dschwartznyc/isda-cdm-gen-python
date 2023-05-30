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

__all__ = ['SubstitutionProvisions']


class SubstitutionProvisions(BaseDataClass):
  """
  Defines collateral substitution provisions such as how many and with how much notice are substitutions allowed.
  """
  noticeDeadlineDateTime: Optional[datetime] = Field(None, description="A specific date and time for the notice deadline")
  """
  A specific date and time for the notice deadline
  """
  noticeDeadlinePeriod: Optional[Period] = Field(None, description="Defines the min period for notify of a substitution.")
  """
  Defines the min period for notify of a substitution.
  """
  numberOfSubstitutionsAllowed: Optional[int] = Field(None, description="Specifies if 1 or more substitutions are allowed.")
  """
  Specifies if 1 or more substitutions are allowed.
  """

from cdm.base.datetime.Period import Period

SubstitutionProvisions.update_forward_refs()
