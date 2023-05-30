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

__all__ = ['TaxonomyValue']


class TaxonomyValue(BaseDataClass):
  """
  Defines a taxonomy value as either a simple string or a more granular expression with class names and values for each class.
  """
  classification: List[TaxonomyClassification] = Field([], description="Specifies the taxonomy value as a set of class names and values for each class.")
  """
  Specifies the taxonomy value as a set of class names and values for each class.
  """
  name: Optional[AttributeWithMeta[str] | str] = Field(None, description="Specifies the taxonomy value as a simple string, which may be associated to an external scheme.")
  """
  Specifies the taxonomy value as a simple string, which may be associated to an external scheme.
  """
  
  @rosetta_condition
  def condition_0_ValueExists(self):
    return (((self.name) is not None) or ((self.classification) is not None))

from cdm.base.staticdata.asset.common.TaxonomyClassification import TaxonomyClassification

TaxonomyValue.update_forward_refs()
