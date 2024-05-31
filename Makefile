.PHONY: help copy-envs setup install requirements pre-commit safety run-local test clean

setup:
	curl -sSL https://install.python-poetry.org | python3 -
	poetry shell

install:
	poetry install --sync

commit:
	pre-commit run --all-files
