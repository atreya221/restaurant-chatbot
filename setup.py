import os
import platform

# rasa installation instructions

if platform.system() == 'Linux':
  os.system('python3 -m pip install virtualenv')
  os.system('python3 -m venv ./venv3')
  os.system('. ./venv3/bin/activate; pip3 install --upgrade pip setuptools wheel')
  os.system('. ./venv3/bin/activate; pip install -r requirements.txt')
else:
  print("Please use LINUX-type OS.")


"""
#rasa installation
python3 -m venv ./venv
. ./venv/bin/activate
pip3 install -U pip
pip3 install -r requirements.txt

#duckling installation
wget -qO- https://get.haskellstack.org/ | sh
sudo apt-get install libpcre3 libpcre3-dev
git clone https://github.com/facebook/duckling.git
cd duckling
stack build

#duckling run

stack exec duckling-example-exe

#rasa run
rasa shell —endpoints endpoints.yml

#actions run
python -m rasa_sdk.endpoint —actions actions
"""