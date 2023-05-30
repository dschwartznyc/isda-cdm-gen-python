#!/bin/sh
function processError() {
  echo ""
  echo ""
  echo "***************************************************************************"
  echo "*                                                                         *"
  echo "*                         INITIALISATION FAILED!                          *"
  echo "*                  -- must be run from root directory --                  *"
  echo "*                                                                         *"
  echo "***************************************************************************"
  echo ""
  exit 1
}

type -P python > /dev/null && PYEXE=python || PYEXE=python3
if ! $PYEXE -c 'import sys; assert sys.version_info >= (3,10)' > /dev/null 2>&1; then
        echo "Found $($PYEXE -V)"
        echo "Expecting at least python 3.10 - exiting!"
        exit 1
fi

ACDIR=$($PYEXE -c "import sys;print('Scripts' if sys.platform.startswith('win') else 'bin')")

MYPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
ROSETTARUNTIMEDIR=$MYPATH/"../runtime"
PYTHONSOURCEDIR=$MYPATH/"../target/python"
VERSION="4_0_0" #or "3_3_2"
cd $PYTHONSOURCEDIR/$VERSION
$PYEXE -m venv --clear .pyenv || processError
source .pyenv/$ACDIR/activate || processError
$PYEXE -m pip install --upgrade pip || processError
$PYEXE -m pip install "setuptools>=62.0" || processError
$PYEXE -m pip install pydantic || processError
$PYEXE -m pip install jsonpickle || processError
$PYEXE -m pip install $ROSETTARUNTIMEDIR/rosetta_runtime-1.0.0-py3-none-any.whl || processError

rm -rf build
$PYEXE -m pip wheel --no-deps --only-binary :all: . || processError
rm -rf build
mv python_cdm-0.0.0-py3-none-any.whl ./$VERSION/
echo ""
echo ""
echo "***************************************************************************"
echo "*                                                                         *"
echo "*                                 SUCCESS!!!                              *"
echo "*                                                                         *"
echo "*Finished installing dependencies and building/installing the cdm package!*"
echo "*                                                                         *"
echo "*                      package placed in target/python                    !*"
echo "*                                                                         *"
echo "***************************************************************************"
echo ""