include .env
export $(shell sed 's/=.*//' .env)

USING_POETRY=$(shell grep "tool.poetry" pyproject.toml && echo "yes")
PY_VERSION := $(shell cat .python-version)

.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "    clean      to remove all generated files."
	@echo "    fmt        to format code using black."
	@echo "    install    to install the project in dev mode."
	@echo "    lint       to lint code using flake8, black, mypy."
	@echo "    test       to run tests using pytest."
	@echo "    venv       to create a virtual environment."

.PHONY: install
install:
	@if [[ "$(USING_POETRY)" ]]; then \
		poetry install; \
	else \
		echo "Poetry is not installed or not being used in this project."; \
	fi

.PHONY: fmt
fmt:
	poetry run black source/

.PHONY: lint
lint:
	poetry run flake8 source/
	poetry run black --check source/
	poetry run mypy --ignore-missing-imports source/

.PHONY: test
test:
	@sh -c 'poetry run pytest || ([ $$? = 5 ] && exit 0 || exit $$?)'

.PHONY: clean
clean:
	@find ./ -name '*~' -exec rm -f {} \;
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;

	@rm -rf .mypy_cache .pytest_cache .tox/ *.egg-info build dist htmlcov .cache

.PHONY: venv
venv:
	@if [[ "$(USING_POETRY)" ]]; then \
		poetry env use $(PY_VERSION); \
		poetry shell --no-interaction; \
	else \
		echo "Poetry is not installed or not being used in this project."; \
	fi

.PHONY: deploy
deploy:
	docker-compose down -v -t 1 --remove-orphans
	docker-compose up --build -d
