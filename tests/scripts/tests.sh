#Start mock server for 'https://www.google.com'
cd ../..
(run_server.py --package tests.mockserver --app google_app --port 8001 &)

source tests/scripts/behave.sh
