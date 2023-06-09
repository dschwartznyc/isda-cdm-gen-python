#!/bin/bash
type -P python > /dev/null && PYEXE=python || PYEXE=python3
if ! $PYEXE -c 'import sys; assert sys.version_info >= (3,10)' > /dev/null 2>&1; then
        echo "Found $($PYEXE -V)"
        echo "Expecting at least python 3.10 - exiting!"
        exit 1
fi

MYPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
ROSETTARUNTIMEDIR="../runtime"
PYTHONCDMDIR="../target/python"
#VERSION="3_3_2"
VERSION="4_0_0"
cd $MYPATH

ACDIR=$(python -c "import sys;print('Scripts' if sys.platform.startswith('win') else 'bin')")

rm -rf testenv

$PYEXE -m venv --clear testenv
source testenv/$ACDIR/activate

$PYEXE -m pip install pytest
$PYEXE -m pip install $MYPATH/$ROSETTARUNTIMEDIR/rosetta_runtime-1.0.0-py3-none-any.whl 
$PYEXE -m pip install $MYPATH/$PYTHONCDMDIR/$VERSION/python_cdm-0.0.0-py3-none-any.whl
$PYEXE serialization/test_identifier.py $VERSION
$PYEXE serialization/test_party.py $VERSION
$PYEXE serialization/test_trade_state_product.py $VERSION