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

__all__ = ['ProductTaxonomy']

from cdm.base.staticdata.asset.common.Taxonomy import Taxonomy

class ProductTaxonomy(Taxonomy):
  """
  Specifies the product taxonomy, which is composed of a taxonomy value and a taxonomy source.
  """
  primaryAssetClass: Optional[AttributeWithMeta[AssetClassEnum] | AssetClassEnum] = Field(None, description="Classifies the most important risk class of the trade.")
  """
  Classifies the most important risk class of the trade.
  """
  productQualifier: Optional[str] = Field(None, description="Derived from the product payout features using a CDM product qualification function that determines the product type based on the product payout features.")
  """
  Derived from the product payout features using a CDM product qualification function that determines the product type based on the product payout features.
  """
  secondaryAssetClass: List[AttributeWithMeta[AssetClassEnum] | AssetClassEnum] = Field([], description=" Classifies additional risk classes of the trade, if any.")
  """
   Classifies additional risk classes of the trade, if any.
  """
  
  @rosetta_condition
  def condition_0_TaxonomyType(self):
    """
    Requires a taxonomy type to be chosen, either from a taxonomy source or using asset classes.
    """
    return self.check_one_of_constraint('source', 'primaryAssetClass', 'secondaryAssetClass', necessity=True)
  
  @rosetta_condition
  def condition_1_TaxonomySource(self):
    """
    A taxonomy source can only be associated with a taxonomy value or productQualifier
    """
    def _then_fn0():
      return (((self.value) is not None) or ((self.productQualifier) is not None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.source) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_TaxonomyValue(self):
    """
    A taxonomy value and product qualifier are mutually exclusive. Choice is optional as it only applies when source exists.
    """
    return self.check_one_of_constraint('value', 'productQualifier', necessity=False)

from cdm.base.staticdata.asset.common.AssetClassEnum import AssetClassEnum

ProductTaxonomy.update_forward_refs()
