# ML_Project

## Virtual Environment

To make it easier to run the same version of python (without actually having it install globally) we're using
[Virtual Env](https://virtualenv.pypa.io/en/stable/).

Install steps (assuming you have pip >= 1.3 installed ):

- Install virtualenv
```bash
$ sudo pip install virtualenv
```

- Get your preferred version of python (3.6)

- Create your venv folder (I only tested this in my Mac. It's probably similar enough to Linux)
```bash
$ virtualenv -p /usr/local/bin/python3.6 venv
```

- Run the virtual env
```bash
$ source venv/bin/activate
```

- Install libraries
```bash
$ pip install -r requirements.txt
```

Phew! That's a lot. That should make this project behave consistently across all of our machines though.
A few things to make sure of:

- When running any python code, make sure you ran the command `source venv/bin/activate`
- If you install any new library, please make sure you're running the virtual environment and add the library to our `requirements.txt`. You'd do so like this: `pip install <package> && pip freeze > requirements.txt`


### TODO

### Data
- I got the data from http://theremin.music.uiowa.edu/MIS.html
