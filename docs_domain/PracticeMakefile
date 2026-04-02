.DEFAULT_GOAL := help

# Переменные
PYTHON = python3
PYTEST = pytest
COV_DIR = htmlcov

.PHONY: help setup clean test test-cov lint format run init

help:
	@echo "Available commands for this practice:"
	@echo "  make init       - Initialize full project structure"
	@echo "  make setup      - Install dependencies"
	@echo "  make clean      - Clean temporary files"
	@echo "  make test       - Run tests"
	@echo "  make test-cov   - Run tests with coverage"
	@echo "  make lint       - Run linter"
	@echo "  make format     - Format code"
	@echo "  make run        - Run main script"

init:
	@echo "Initializing project structure..."
	mkdir -p src tests docs
	touch README.md requirements.txt
	touch docs/DOMAIN.md
	touch src/main.py tests/test_main.py
	@echo "Creating sample files..."
	@echo '# Documentation for DOMAIN' > docs/DOMAIN.md
	@echo 'def main():' > src/main.py
	@echo '    print("Hello from practice!")' >> src/main.py
	@echo '' >> src/main.py
	@echo 'if __name__ == "__main__":' >> src/main.py
	@echo '    main()' >> src/main.py
	@echo '"""Sample test file."""' > tests/test_main.py
	@echo 'from src.main import main' >> tests/test_main.py
	@echo '' >> tests/test_main.py
	@echo 'def test_main():' >> tests/test_main.py
	@echo '    assert main() is None' >> tests/test_main.py
	@echo '# Practice requirements' > requirements.txt
	@echo 'pytest>=7.0.0' >> requirements.txt
	@echo 'Project structure initialized successfully!'
	@echo ""
	@echo "Next steps:"
	@echo "  1. Edit src/main.py - your main code"
	@echo "  2. Edit tests/test_main.py - your tests"
	@echo "  3. Run 'make setup' to install dependencies"
	@echo "  4. Run 'make test' to run tests"

setup:
	pip install -r requirements.txt
	pip install -e .

clean:
	rm -rf __pycache__
	rm -rf $(COV_DIR)
	rm -rf .pytest_cache
	rm -rf *.egg-info
	rm -rf build dist
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

test:
	$(PYTHON) -m $(PYTEST) -v

test-cov:
	$(PYTHON) -m $(PYTEST) --cov=. --cov-report=html --cov-report=term -v
	@echo "Coverage report generated in $(COV_DIR)/index.html"

lint:
	$(PYTHON) -m flake8 src tests --max-line-length=120
	$(PYTHON) -m pylint src --exit-zero

format:
	$(PYTHON) -m black src tests --line-length=120
	$(PYTHON) -m isort src tests

run:
	$(PYTHON) src/main.py
