#Start mock server for 'https://www.google.com'
echo $PWD
(coverage run --rcfile=tests/.coveragerc run_server.py --package tests.mockserver --app google_app --port 8001 &)

source tests/scripts/behave.sh
