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

__all__ = ['TradeIdentifier']

from cdm.base.staticdata.identifier.Identifier import Identifier

class TradeIdentifier(Identifier):
  """
  Defines a trade identifier as a special case of the generic identifier type, that also includes the trade identifier class.
  """
  identifierType: Optional[TradeIdentifierTypeEnum] = Field(None, description="The enumerated classification of the identifier. Optional as a trade identifier may be party-specific, in which case it may not correspond to any established classification.")
  """
  The enumerated classification of the identifier. Optional as a trade identifier may be party-specific, in which case it may not correspond to any established classification.
  """

from cdm.base.staticdata.identifier.TradeIdentifierTypeEnum import TradeIdentifierTypeEnum

TradeIdentifier.update_forward_refs()
