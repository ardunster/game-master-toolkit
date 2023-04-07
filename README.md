# game-master-toolkit

Tools for TTRPG Game Masters.

[//]: # (TODO: How to set up repo for use only, vs how to set up for contribution.)

[//]: # (TODO: What do I need in setup.py?)

## Installation

```bash
pipenv install
```

??? - jsonschema is required at least, so some kind of install is necessary.

## Running The Toolkit

To run the entire toolkit, you need only run the package from the root directory of the repository:

```bash
game-master-toolkit % python3.9 -m game_master_toolkit
```

## Contributing

### Install dependencies

pipenv install --dev

### Setup pre-commit and pre-push hooks

pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push

### Development Practices

This repository was created using Python 3.9.16, and using pipenv to manage packages. It uses Black and isort to
standardize formatting and imports, and Flake8 for linting.
The [Best Practices Tutorial on Sourcery](https://sourcery.ai/blog/python-best-practices/) was followed for the majority
of basic setup.

To set up pre-commit hooks, please run `pre-commit install` in this repository after installing modules.

To run:

- tests without coverage report: `pipenv run pytest`
- tests with coverage report: `pipenv run pytest --cov --cov-fail-under=100`
- Black: `pipenv run black`
- isort: `pipenv run isort`
- flake8: `pipenv run flake8`

[//]: # (TODO: investigate whether adding mypy is worthwhile.)
