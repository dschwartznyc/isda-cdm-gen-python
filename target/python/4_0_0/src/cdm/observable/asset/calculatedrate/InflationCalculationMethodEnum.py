from enum import Enum

all = ['InflationCalculationMethodEnum']
  
class InflationCalculationMethodEnum(Enum):
  """
  Indicates how to use the inflation index to calculate the payment (e.g. Ratio, Return, Spread). Added for Inflation Asset Swap
  """
  RATIO = "RATIO"
  """
  (Inflation Index Final / Inflation Index Base). Inflation Index Final is inflation index for Reference Month that is the Lag number of months prior to Payment Date (subject to interpolation). Inflation Index Base subject to the Calculation Style. Used in inflation asset swaps to calculate the inflation coupons and principal exchange.
  """
  RETURN = "RETURN"
  """
  (Inflation Index Final / Inflation Index Base -1). Inflation Index Final is the inflation index for Reference Month that is the Lag number of months prior to Payment Date (subject to interp). Inflation Index Base subject to the Calculation Style. Used in market standard ZC Inflation swaps.
  """
  SPREAD = "SPREAD"
  """
  Inflation Index Final - Inflation Index Base). Inflation Index Final is Index for Ref month the Lag months prior to Payment Date (subject to interp). Inflation Index Base subject to the Calculation Style. Typically used for fixing locks.
  """
