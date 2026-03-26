VENV := .venv
PYTHON := $(VENV)/Scripts/python
PIP := $(VENV)/Scripts/pip

$(VENV)/Scripts/python:
	python -m venv $(VENV)
	$(PIP) install --upgrade pip

install: $(VENV)/Scripts/python
	$(PIP) install -r requirements.txt

run: install
	$(PYTHON) src/app.py

check-deps: install
	$(PYTHON) scripts/check_requirements.py

typecheck: install
	$(PYTHON) -m mypy src/

format: install
	$(PYTHON) -m black src/

lint: install
	$(PYTHON) -m flake8 src/

check: typecheck check-deps lint
	@echo "All checks passed"

clean:
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

.PHONY: install run check-deps typecheck format lint check clean