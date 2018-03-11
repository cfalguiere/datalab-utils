ANACONDA_PATH=/C/Tools/Anaconda2
export PYTHON_PATH=${ANACONDA_PATH}/envs/anaconda-env-27

python -m unittest sch.common.app_test
python -m unittest sch.common.exceptions_test
python -m unittest sch.common.rutils_test
python -m unittest sch.common.validator_test

python -m unittest sch.init.configuration_test
