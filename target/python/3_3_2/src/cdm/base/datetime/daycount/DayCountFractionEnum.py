from enum import Enum

all = ['DayCountFractionEnum']
  
class DayCountFractionEnum(Enum):
  """
  The enumerated values to specify the day count fraction.
  """
  ACT_360 = "ACT/360"
  """
  Per 2006 ISDA Definitions, Section 4.16. Day Count Fraction, paragraph (e) or Annex to the 2000 ISDA Definitions (June 2000 Version), Section 4.16. Day Count Fraction, paragraph (d).
  """
  ACT_364 = "ACT/364"
  """
  Per CFTC definitions.
  """
  ACT_365L = "ACT/365L"
  """
  Per 2006 ISDA Definitions, Section 4.16. Day Count Fraction, paragraph (i).
  """
  ACT_365_FIXED = "ACT/365.FIXED"
  """
  Per 2006 ISDA Definitions, Section 4.16. Day Count Fraction, paragraph (d) or Annex to the 2000 ISDA Definitions (June 2000 Version), Section 4.16. Day Count Fraction, paragraph (c).
  """
  ACT_ACT_AFB = "ACT/ACT.AFB"
  """
  The Fixed/Floating Amount will be calculated in accordance with the 'BASE EXACT/EXACT' day count fraction, as defined in the 'Definitions Communes plusieurs Additifs Techniques' published by the Association Francaise des Banques in September 1994.
  """
  ACT_ACT_ICMA = "ACT/ACT.ICMA"
  """
  Per 2006 ISDA Definitions, Section 4.16. Day Count Fraction, paragraph (c). This day count fraction code is applicable for transactions booked under the 2006 ISDA Definitions. Transactions under the 2000 ISDA Definitions should use the ACT/ACT.ISMA code instead.
  """
  ACT_ACT_ISDA = "ACT/ACT.ISDA"
  """
  Per 2006 ISDA Definitions, Section 4.16. Day Count Fraction, paragraph (b) or Annex to the 2000 ISDA Definitions (June 2000 Version), Section 4.16. Day Count Fraction, paragraph (b). Note that going from FpML 2.0 Recommendation to the FpML 3.0 Trial Recommendation the code in FpML 2.0 'ACT/365.ISDA' became 'ACT/ACT.ISDA'.
  """
  ACT_ACT_ISMA = "ACT/ACT.ISMA"
  """
  The Fixed/Floating Amount will be calculated in accordance with Rule 251 of the statutes, by-laws, rules and recommendations of the International Securities Market Association, as published in April 1999, as applied to straight and convertible bonds issued after December 31, 1998, as though the Fixed/Floating Amount were the interest coupon on such a bond. This day count fraction code is applicable for transactions booked under the 2000 ISDA Definitions. Transactions under the 2006 ISDA Definitions should use the ACT/ACT.ICMA code instead.
  """
  BUS_252 = "BUS/252"
  """
  The number of Business Days in the Calculation Period or Compounding Period in respect of which payment is being made divided by 252.
  """
  RBA_BOND_BASIS_ANNUAL = "RBA Bond Basis (annual)"
  """
  Per 2006 ISDA Definitions Supplement number 43, Day Count Fraction, (k)  if 'RBA Bond Basis (semi-annual)' is specified, 0.5. However, Actual/Actual (ISDA) applies to each of the first Calculation Period and the final Calculation Period if such Calculation Period is less than six months
  """
  RBA_BOND_BASIS_QUARTER = "RBA Bond Basis (quarter)"
  """
  Per 2006 ISDA Definitions Supplement number 43, Day Count Fraction, if 'RBA Bond Basis (quarter)' is specified, 0.25. However, Actual/Actual (ISDA) applies to each of the first Calculation Period and the final Calculation Period if such Calculation Period is less than three months
  """
  RBA_BOND_BASIS_SEMI_ANNUAL = "RBA Bond Basis (semi-annual)"
  """
  Per 2006 ISDA Definitions Supplement number 43, Day Count Fraction, if 'RBA Bond Basis (semi-annual)' is specified, 0.5. However, Actual/Actual (ISDA) applies to each of the first Calculation Period and the final Calculation Period if such Calculation Period is less than six months
  """
  _1_1 = "1/1"
  """
  Per 2006 ISDA Definitions, Section 4.16. Day Count Fraction, paragraph (a) or Annex to the 2000 ISDA Definitions (June 2000 Version), Section 4.16. Day Count Fraction, paragraph (a).
  """
  _30E_360 = "30E/360"
  """
  Per 2006 ISDA Definitions, Section 4.16. Day Count Fraction, paragraph (g) or Annex to the 2000 ISDA Definitions (June 2000 Version), Section 4.16. Day Count Fraction, paragraph (f). Note that the algorithm defined for this day count fraction has changed between the 2000 ISDA Definitions and 2006 ISDA Definitions. See Introduction to the 2006 ISDA Definitions for further information relating to this change.
  """
  _30E_360_ISDA = "30E/360.ISDA"
  """
  Per 2006 ISDA Definitions, Section 4.16. Day Count Fraction, paragraph (h). Note the algorithm for this day count fraction under the 2006 ISDA Definitions is designed to yield the same results in practice as the version of the 30E/360 day count fraction defined in the 2000 ISDA Definitions. See Introduction to the 2006 ISDA Definitions for further information relating to this change.
  """
  _30_360 = "30/360"
  """
  Per 2006 ISDA Definitions, Section 4.16. Day Count Fraction, paragraph (f) or Annex to the 2000 ISDA Definitions (June 2000 Version), Section 4.16. Day Count Fraction, paragraph (e).
  """
