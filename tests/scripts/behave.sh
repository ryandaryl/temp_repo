trap 'exit 0' SIGINT SIGQUIT SIGTERM
(sleep 5 && cd tests && behave && kill $$ &)
timeout 30 coverage run --rcfile=tests/.coveragerc run_server.py --package project


#This script is necessary to test the server and obtain coverage results.
#The standard way to test a server is this:
#(python run_server.py &) behave
#But it fails when "coverage" is used instead of "python",
#because coverage.py cannot be ran as a subprocess.
#To work around this, the test runner "behave" is ran as a subprocess instead.

#Line 1: Tell main process to exit OK if it is stopped with "kill"
#Line 2: Run behave as a subprocess. It only kills the main process if all the tests pass.
#Line 3: Run the server under "coverage.py". The timeout stops the server,
# but it does not trigger the trap. So, if the tests fail or they take too long,
# then the main process returns the EXIT_TIMEOUT error code.
# This ensures the main process exit code matches the result of the behave tests.

#TODO: Remove hard-coded test timeout 30. Get it from command line arguments instead.
