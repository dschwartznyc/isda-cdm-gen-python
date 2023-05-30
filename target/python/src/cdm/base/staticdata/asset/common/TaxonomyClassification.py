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

__all__ = ['TaxonomyClassification']


class TaxonomyClassification(BaseDataClass):
  className: str = Field(..., description="The name defined by the classification system for a specific attribute in the taxonomy.")
  """
  The name defined by the classification system for a specific attribute in the taxonomy.
  """
  description: Optional[str] = Field(None, description="A descuription of the class.")
  """
  A descuription of the class.
  """
  value: str = Field(..., description="The value set by the taxonomu that is specific to the className attribute.")
  """
  The value set by the taxonomu that is specific to the className attribute.
  """


TaxonomyClassification.update_forward_refs()
