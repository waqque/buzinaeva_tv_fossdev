VENV := .venv
PYTHON := $(VENV)/Scripts/python
PIP := $(VENV)/Scripts/pip

src:
	mkdir -p src
	echo 'def add(a: int, b: int) -> int:' > src/calc.py
	echo '    return a + b' >> src/calc.py
	echo 'result = add(2, 3)' >> src/calc.py
	echo 'print(result)' >> src/calc.py
	echo 'import requests' > src/service.py
	echo 'import os' >> src/service.py
	echo 'def main():' >> src/service.py
	echo '    print("service")' >> src/service.py
	echo 'requests' > requirements.txt
	echo 'mypy' >> requirements.txt
	echo 'flake8' >> requirements.txt

$(VENV)/Scripts/python: src
	python -m venv $(VENV)
	$(PIP) install --upgrade pip

install: $(VENV)/Scripts/python
	$(PIP) install -r requirements.txt

typecheck: install
	$(PYTHON) -m mypy src/calc.py src/service.py

lint: install
	$(PYTHON) -m flake8 src/calc.py src/service.py

check: typecheck lint
	@echo "ok"

clean:
	rm -rf $(VENV) src requirements.txt