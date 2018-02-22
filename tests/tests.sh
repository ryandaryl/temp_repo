#Start mock server for 'https://www.google.com'
(gunicorn --bind 0.0.0.0:8001 tests:google_app &)

source tests/behave.sh
