# Python3.12
# Formatted to VS Code Black Formatter defualt setting
# Linted with Flake8
# Developed on Mac OS 13.4.1 with x86 CPU

If you want to set up a virtual environment to run the
app run:
	python -m venv .venv
	source .venv/bin/activate
    python main.py

To install the application into your PATH, navigate to 
the project directory in the terminal and run:
    
	python setup.py install

Then you will be able to run the application like in the
prompt.


To run the unit tests, navigate to project directory and 
run:
	python tests.py


Note: the only external dependency is 'setuptools' and
can be installed from requirements.txt or pip directly.
It is only needed to install the app.

