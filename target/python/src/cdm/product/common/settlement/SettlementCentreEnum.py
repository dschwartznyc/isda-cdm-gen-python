from enum import Enum

all = ['SettlementCentreEnum']
  
class SettlementCentreEnum(Enum):
  """
  Defines the settlement centre for a securities transaction.
  """
  CLEARSTREAM_BANKING_LUXEMBOURG = "CLEARSTREAM_BANKING_LUXEMBOURG"
  """
  ClearStream Banking Luxembourg
  """
  EUROCLEAR_BANK = "EUROCLEAR_BANK"
  """
  Euroclear Bank
  """
