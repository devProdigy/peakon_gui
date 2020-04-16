# Quiz app

Python3/Tkinter desktop GUI app for making a quiz.  
This app uses Sqlite3 to store data.

## Prepare
####
Pre-requirements: Python3.7+ should already be installed. 

#### Install Tkinter
Mac:
> brew install tcl-tk

Windows:  
https://stackoverflow.com/questions/20044559/how-to-pip-or-easy-install-tkinter-on-windows

#### Install dependencies
> virtualenv venv --python=/usr/local/bin/python3.7
> source .venv/bin/activate  
> pip install -r app/requirements/requirements.txt

## Run app
> source .venv/bin/activate  
> python3 app/run.py


## Compile with Pyinstaller
> source .venv/bin/activate  
> invoke build
