# This makefile contains commands needed for developer work.
# There shouldn't be complex logic here. If You need logic, write a shell or Python script and run it.
#
# (michalb) This Makefile is a work in progress.
#
# MANUAL:
# Passing a parameter (e.g. PYTEST_ARGS) to a Makefile target(e.g. `test:`): `make test PYTEST_ARGS="-k happy_path"

SHELL:=/bin/bash

SRC_DIRECTORIES:=netbox_plugins
DOCKER_CODE_DIR:=/opt/code/netbox_plugins/

# No pytest args by default.
PYTEST_ARGS:=
PYTEST_PATH:=/opt/code/netbox_plugins/netbox-custom-scripts

# Use double hash symbol '##' after the target name to specify the help text for that target
.PHONY: help
help:  ## Print Makefile targets.
	@echo Available Makefile targets:
	@sed -ne 's/^\([^[:space:]]*\):.*##/\1:\t/p' $(MAKEFILE_LIST) | column -t -s $$'\t'

.PHONY: setup_venv
setup_venv:  ## Set up a virtual environment for IDE's code completion tools.
	python3.11 -m venv .venv
	.venv/bin/pip install -r requirements-local-dev.txt

.PHONY: run
run:  ## Run Netbox locally.
	docker compose up -d --build

.PHONY: destroy
destroy:  ## Stop all containers (including Netbox), wipe data.
	docker compose down -v --remove-orphans

.PHONY: restart
restart:  ## Restart Netbox container.
	docker compose restart netbox

.PHONY: reload
reload:  ## Reload Netbox server process.
	docker compose exec netbox curl -X GET --unix-socket /opt/unit/unit.sock http://localhost/control/applications/netbox/restart

.PHONY: check
check: static_analysis test  ## Full quality checks for Netbox.

.PHONY: test
test:  ## Run Netbox tests.
	@echo ===============================
	@echo Tests
	@echo ===============================
	docker compose run --rm netbox pytest $(PYTEST_PATH) $(PYTEST_ARGS)

.PHONY: static_analysis
static_analysis:  ## Perform Ruff formatting and linting.
	@echo ===============================
	@echo Ruff formatting check + linting
	@echo ===============================
	docker compose run --rm netbox bash -c "cd $(DOCKER_CODE_DIR); ruff format --check --diff && ruff check"

.PHONY: format
format:  ## Perform Ruff formatting and import sorting.
	@echo =================================
	@echo Formatting code + sorting imports
	@echo =================================
	docker compose run --rm netbox bash -c "cd $(DOCKER_CODE_DIR); ruff format && ruff check --select I --fix"

.PHONY:
make_migrations:  ## Create Django DB migrations.
	@echo =============================
	@echo Creating Django DB migrations
	@echo =============================
	docker compose run --rm netbox python manage.py makemigrations

# Utility commands =========================

.PHONY: shell
shell:  ## Open linux shell inside Netbox container.
	docker compose exec netbox bash

.PHONY: shell-netbox
shell-netbox:  ## Open Netbox shell.
	docker compose exec netbox python manage.py nbshell

.PHONY: shell-db
shell-db:    ## Open PostgreSQL interactive shell.
	docker compose exec postgres bash -c "PGPASSWORD=netbox psql -U netbox -d netbox"
