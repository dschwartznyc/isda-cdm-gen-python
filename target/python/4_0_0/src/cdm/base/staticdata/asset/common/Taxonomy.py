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

__all__ = ['Taxonomy']


class Taxonomy(BaseDataClass):
  """
  Defines the taxonomy of an object by combining a taxonomy source (i.e. the rules to classify the object) and a value (i.e. the output of those rules on the object).
  """
  source: Optional[TaxonomySourceEnum] = Field(None, description="The source of the taxonomy that defines the rules for classifying the object. The taxonomy source is taken from a enumerated list of taxonomy names. Optional as the taxonomy source may not be provided.")
  """
  The source of the taxonomy that defines the rules for classifying the object. The taxonomy source is taken from a enumerated list of taxonomy names. Optional as the taxonomy source may not be provided.
  """
  value: Optional[TaxonomyValue] = Field(None, description="The value according to that taxonomy. Optional as it may not be possible to classify the object in that taxonomy.")
  """
  The value according to that taxonomy. Optional as it may not be possible to classify the object in that taxonomy.
  """

from cdm.base.staticdata.asset.common.TaxonomySourceEnum import TaxonomySourceEnum
from cdm.base.staticdata.asset.common.TaxonomyValue import TaxonomyValue

Taxonomy.update_forward_refs()
