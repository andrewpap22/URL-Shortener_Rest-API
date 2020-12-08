# remove any existing caches
rm -rf ./venv/

# install python 3 virtual enviroment
virtualenv venv -p python3 

# 'activate' the virtual enviroment on the working shell 
source ./venv/bin/activate

# install requirements
pip3 install -r ./requirements.txt

# run the server 
python3 ./run.py