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

__all__ = ['CancelableProvision']

from cdm.base.staticdata.party.BuyerSeller import BuyerSeller

class CancelableProvision(BuyerSeller):
  """
  A data defining:  the right of a party to cancel a swap transaction on the specified exercise dates. The provision is for 'walk-away' cancellation (i.e. the fair value of the swap is not paid). A fee payable on exercise can be specified. As a difference from the FpML construct, the canonical model extends the BuyerSeller class.
  """
  americanExercise: Optional[AmericanExercise] = Field(None, description="American exercise. FpML implementations consists in an exercise substitution group.")
  """
  American exercise. FpML implementations consists in an exercise substitution group.
  """
  bermudaExercise: Optional[BermudaExercise] = Field(None, description="Bermuda exercise. FpML implementations consists in an exercise substitution group.")
  """
  Bermuda exercise. FpML implementations consists in an exercise substitution group.
  """
  callingParty: Optional[CallingPartyEnum] = Field(None, description="The party with right to exercise a cancellation. Allows for buyer, seller or either.")
  """
  The party with right to exercise a cancellation. Allows for buyer, seller or either.
  """
  cancelableProvisionAdjustedDates: Optional[CancelableProvisionAdjustedDates] = Field(None, description="The adjusted dates associated with a cancelable provision. These dates have been adjusted for any applicable business day convention.")
  """
  The adjusted dates associated with a cancelable provision. These dates have been adjusted for any applicable business day convention.
  """
  earliestCancellationTime: Optional[BusinessCenterTime] = Field(None, description="The earliest time in a business day that notice of cancelation can be given.")
  """
  The earliest time in a business day that notice of cancelation can be given.
  """
  earliestDate: Optional[AdjustableOrRelativeDate] = Field(None, description="The first day when cancelation is permitted to take effect. A party may give notice prior to this date and taken together with the effective period would be necessary to cancel on this date.")
  """
  The first day when cancelation is permitted to take effect. A party may give notice prior to this date and taken together with the effective period would be necessary to cancel on this date.
  """
  effectiveDate: Optional[AdjustableOrRelativeDates] = Field(None, description="The effective date if cancelation is invoked otherwise the cancellation period defines the cancellation date.")
  """
  The effective date if cancelation is invoked otherwise the cancellation period defines the cancellation date.
  """
  effectivePeriod: Optional[Period] = Field(None, description="Effective period for cancelation when notice is given. This is the period after notice is given that cancellation becomes effecticve.")
  """
  Effective period for cancelation when notice is given. This is the period after notice is given that cancellation becomes effecticve.
  """
  europeanExercise: Optional[EuropeanExercise] = Field(None, description="European exercise. FpML implementations consists in an exercise substitution group.")
  """
  European exercise. FpML implementations consists in an exercise substitution group.
  """
  exerciseNotice: Optional[ExerciseNotice] = Field(None, description="Definition of the party to whom notice of exercise should be given.")
  """
  Definition of the party to whom notice of exercise should be given.
  """
  expirationDate: Optional[AdjustableOrRelativeDate] = Field(None, description="The last day within the term of the contract that cancelation is allowed.")
  """
  The last day within the term of the contract that cancelation is allowed.
  """
  finalCalculationPeriodDateAdjustment: List[FinalCalculationPeriodDateAdjustment] = Field([], description="Business date convention adjustment to final payment period per leg (swapStream) upon exercise event. The adjustments can be made in-line with leg level BDC's or they can be specified separately.")
  """
  Business date convention adjustment to final payment period per leg (swapStream) upon exercise event. The adjustments can be made in-line with leg level BDC's or they can be specified separately.
  """
  followUpConfirmation: bool = Field(..., description="A flag to indicate whether follow-up confirmation of exercise (written or electronic) is required following telephonic notice by the buyer to the seller or seller's agent.")
  """
  A flag to indicate whether follow-up confirmation of exercise (written or electronic) is required following telephonic notice by the buyer to the seller or seller's agent.
  """
  initialFee: Optional[Transfer] = Field(None, description="An initial fee for the cancelable option.")
  """
  An initial fee for the cancelable option.
  """
  latestCancelationTime: Optional[BusinessCenterTime] = Field(None, description="The latest time at which notice of cancelation can be given.")
  """
  The latest time at which notice of cancelation can be given.
  """
  
  @rosetta_condition
  def condition_0_EffectiveDate(self):
    """
    Must select one of predefined cancellation types of effectiveDate or effectivePeriod.
    """
    return self.check_one_of_constraint('effectiveDate', 'effectivePeriod', necessity=False)
  
  @rosetta_condition
  def condition_1_CancelableProvisionExerciseNoticeReceiverParty(self):
    def _then_fn0():
      return all_elements(self.exerciseNotice.exerciseNoticeReceiver, "=", AncillaryRoleEnum.EXERCISE_NOTICE_RECEIVER_PARTY_CANCELABLE_PROVISION)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.exerciseNotice.exerciseNoticeReceiver) is not None), _then_fn0, _else_fn0)

from cdm.product.template.AmericanExercise import AmericanExercise
from cdm.product.template.BermudaExercise import BermudaExercise
from cdm.product.template.CallingPartyEnum import CallingPartyEnum
from cdm.product.template.CancelableProvisionAdjustedDates import CancelableProvisionAdjustedDates
from cdm.base.datetime.BusinessCenterTime import BusinessCenterTime
from cdm.base.datetime.AdjustableOrRelativeDate import AdjustableOrRelativeDate
from cdm.base.datetime.AdjustableOrRelativeDates import AdjustableOrRelativeDates
from cdm.base.datetime.Period import Period
from cdm.product.template.EuropeanExercise import EuropeanExercise
from cdm.product.template.ExerciseNotice import ExerciseNotice
from cdm.product.common.schedule.FinalCalculationPeriodDateAdjustment import FinalCalculationPeriodDateAdjustment
from cdm.event.common.Transfer import Transfer
from cdm.base.staticdata.party.AncillaryRoleEnum import AncillaryRoleEnum

CancelableProvision.update_forward_refs()
