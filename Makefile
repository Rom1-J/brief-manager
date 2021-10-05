VIRTUAL_ENV := venv
PYTHON_PATH := $(VIRTUAL_ENV)/bin/python

########################################################################################################################
# Init
########################################################################################################################

.PHONY: main
main: install
	$(VIRTUAL_ENV)/bin/pip install -U pip setuptools

.PHONY: install
install:
	$(VIRTUAL_ENV)/bin/pip install .

.PHONY: install-dev
install-dev:
	$(VIRTUAL_ENV)/bin/pip install -r requirements/dev.txt

.PHONY: run
run:
	$(VIRTUAL_ENV)/bin/brief

.PHONY: dev
dev: style update run

.PHONY: update
update:
	$(VIRTUAL_ENV)/bin/pip install --upgrade .

.PHONY: update-all
update-all:
	$(VIRTUAL_ENV)/bin/pip install --upgrade --force-reinstall .


########################################################################################################################
# Style code
########################################################################################################################

.PHONY: black
black:
	$(PYTHON_PATH) -m black `git ls-files "*.py"` --line-length=79

.PHONY: lint
lint:
	$(PYTHON_PATH) -m pylint brief --verbose --output-format=colorized

.PHONY: type
type:
	$(PYTHON_PATH) -m mypy brief

.PHONY: style
style: black lint type
