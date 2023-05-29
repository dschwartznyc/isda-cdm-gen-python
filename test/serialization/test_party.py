import pytest
from cdm.base.staticdata.party.Party import Party
import sys,os
dirPath = os.path.dirname(__file__)
sys.path.append(os.path.join(dirPath))
from cdm_comparison_test import cdm_comparison_test_from_file

def test_party ():
	cdm_comparison_test_from_file(dirPath + '/cdm_samples_3_3_2/original_Party.json', Party)

if __name__ == "__main__":
	test_party()