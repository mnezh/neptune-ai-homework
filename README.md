# The API testing example

* Based on the requirements specified in [assignment/README.md](assignment/README.md)
* Discovered the bugs listed in [bugs](bugs)

## Setup
Prerequisites: 
* [recent](https://devguide.python.org/versions/) Python, most probably 3.11+ would work fine.
* GNU make
* Tested on OS X, most probably would work on Linux, precautions were made for GNU make to work on Windows, though not tested

To create a python virtual environment and install all dependencies:
```shell
$ make setup
```

To configure target environment details, create a `.env` file:
```shell
BASE_URL=https://o2x5b-4a3w-1xb2-dot-neptune-sandbox-441620.lm.r.appspot.com
API_TOKEN=your-token
```

## Run tests

```shell
$ make test
...
tests/test_auth.py:

Authentication:
  » No authorization header not accepted
  ✓ Basic authentication not accepted
  ✓ Invalid bearer token not accepted
  ✓ Valid token accepted
```
