PYTHON_VERSION ?= 3.11.5
POETRY_VERSION ?= 1.0.1

.PHONY: build publish

build:
	poetry build

publish:
	poetry config pypi-token.pypi ${PYPI_TOKEN}
	poetry publish --build

