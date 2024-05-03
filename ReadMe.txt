In order for tasks.py to work, you need to localy set up Locust and enter tasks.py inside the directory. Use the following commands:
mkdir /tmp/locust
cd /tmp/locust
python3 -m venv env
source env/bin/activate
pip install locust


To launch Locust, use the following command:
locust -f tasks.py

To launch nbad.py use the following command:
python nbad.py


!For MacOS if the python nbad.py command does not work, use the following:
python3 nbad.py

everything else can be found in the Appendices,
Thank you
