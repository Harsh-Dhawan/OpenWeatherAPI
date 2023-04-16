from behave import __main__ as behave_runner

'''
This file is alternative for running behave CLI commands from Terminal in order to run BDD test cases
'''

if __name__ == '__main__':
    parameter = ' --no-capture --no-capture-stderr --no-logcapture --show-timings'
    behave_runner.main(parameter)


