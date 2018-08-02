conpango
=========

Beer Manager API


Requirements:
-------------

Please make sure the following things are properly installed on your computer.

- [python](https://python.org/downloads/>)
- [virtualenv](https://virtualenv.pypa.io/en/stable/>)

Getting Started
---------------

1. Clone the repo

```
$ git clone https://github.com/Ntu2koTrevor/canpango
$ cd conpango
```

2. Setup the VirtualEnv

```
$ virtualenv ve
$ source ve/bin/activate
```

3. Install requirements

```
$ pip install -e .
```

4. Setup database and run

$ cd beerapi
$ ./manage.py migrate
$ ./manage.py createsuperuser
$ ./manage.py runserver
```

You can now access the demo site on http://localhost:8000
