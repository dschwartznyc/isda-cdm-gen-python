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

__all__ = ['AssetPayout']

from cdm.product.common.settlement.PayoutBase import PayoutBase

class AssetPayout(PayoutBase):
  """
  Security finance payout specification in case the product payout involves some form of security collateral, as in a securities financing transaction. Plus additional description for ICMA.
  """
  assetLeg: List[AssetLeg] = Field([], description="Defines each asset movement as a buy/sell at different dates, typically 1 near leg and 1 far leg in a securities financing transaction.")
  """
  Defines each asset movement as a buy/sell at different dates, typically 1 near leg and 1 far leg in a securities financing transaction.
  """
  @rosetta_condition
  def cardinality_assetLeg(self):
    return check_cardinality(self.assetLeg, 1, None)
  
  dividendTerms: Optional[DividendTerms] = Field(None, description="Specifies the terms under which dividends received by the borrower are passed through to the lender.")
  """
  Specifies the terms under which dividends received by the borrower are passed through to the lender.
  """
  durationType: Duration = Field(..., description="Specifies the Duration Terms of the Security Finance transaction. e.g. Open or Term.")
  """
  Specifies the Duration Terms of the Security Finance transaction. e.g. Open or Term.
  """
  minimumFee: Optional[Money] = Field(None, description="A contractual minimum amount which the borrower will pay, regardless of the duration of the loan. A mechanism for making sure that a trade generates enough income.")
  """
  A contractual minimum amount which the borrower will pay, regardless of the duration of the loan. A mechanism for making sure that a trade generates enough income.
  """
  securityInformation: Product = Field(..., description="Specifies the Purchased Security.  Within SecurityPayout we include a condition which validates that the product must be a Security (see below condition 'ProductMustBeSecurity').")
  """
  Specifies the Purchased Security.  Within SecurityPayout we include a condition which validates that the product must be a Security (see below condition 'ProductMustBeSecurity').
  """
  
  @rosetta_condition
  def condition_0_Quantity(self):
    """
    When there is an OptionPayout the quantity can be expressed as part of the payoutQuantity, or as part of the underlier in the case of a Swaption.  For all other payouts that extend PayoutBase the payoutQuantity is a mandatory attribute.
    """
    return ((self.priceQuantity) is not None)
  
  @rosetta_condition
  def condition_1_ProductMustBeSecurity(self):
    """
    Validates that the Purchased Security must be a security.
    """
    return ((self.securityInformation.security) is not None)
  
  @rosetta_condition
  def condition_2_DividendTermsValidation(self):
    """
    Validates that if the transaction has Dividend Terms specified then the Duration should be Term.
    """
    def _then_fn0():
      return all_elements(self.durationType.durationType, "=", DurationTypeEnum.TERM)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.dividendTerms) is not None), _then_fn0, _else_fn0)

from cdm.product.template.AssetLeg import AssetLeg
from cdm.product.template.DividendTerms import DividendTerms
from cdm.product.template.Duration import Duration
from cdm.observable.asset.Money import Money
from cdm.product.template.Product import Product
from cdm.product.template.DurationTypeEnum import DurationTypeEnum

AssetPayout.update_forward_refs()
