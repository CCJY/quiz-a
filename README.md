# quiz-a

The code was tested on Ubuntu 20.04.

## Requirements

- api_endpoint
- auth_token
- data.json
- python 3.8.5

## Get Started

### Install python packages

```
sudo apt-get install python3-venv
```

```
python3 -m venv .venv
```

```
source .venv/bin/activate
```

```
pip install -r requirements.txt
```

### Run tests

- Add api_endpoint and auth_token on tests/test_offers.py

- Copy and past data.json on root folder

```
python -m unittest tests
```
