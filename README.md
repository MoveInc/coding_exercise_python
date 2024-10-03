# Anagram Finder Python exercise

This notional exercise implements a basic API which returns all anagrams of a given word based on an internal word dictionary. At least, that's what it's supposed to do. Continue reading for more details.

## Development

### Scripts

* `python3 -m venv localenv` - create local virtual env
* `source localenv/bin/activate` - enable virtual env shell
* `pip install -r requirements.txt` - install dependencies
* `pip install -r requirements_dev.txt` - install development dependencies for testing
* `pytest` - run unit tests
* `flask run` - run local server

## REST Service

After starting the server, the REST endpoint can be invoked using http://localhost:5000/?term=word where '**word**' is the term to find anagrams for. The response should be a JSON payload containing a string array of all matching anagrams.

## Problems

This project has the following issues:

* The included unit test fails
* The endpoint doesn't return correct results

Please ensure all problems are resolved as part of this exercise.
