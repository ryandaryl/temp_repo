#Start mock server for 'https://www.google.com'
echo $PWD
(../run_server.py --package mockserver --app google_app --port 8001 &)

source tests/scripts/behave.sh
