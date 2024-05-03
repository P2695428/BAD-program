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

The host for the nbad.py website is:
Http://127.0.0.1:5000

The host for the locust framework is:
Http://127.0.0.1:8089

The test server (http-server command) is:
Http://127.0.0.1:8080 (For Locust test purposes only)


everything else can be found in the Appendices,
Thank you
