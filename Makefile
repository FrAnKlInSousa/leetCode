setup:
	curl -sSL https://install.python-poetry.org | python3 -
	poetry shell

install:
	poetry install --sync