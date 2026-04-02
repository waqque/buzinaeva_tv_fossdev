.DEFAULT_GOAL := help

.PHONY: create-practice remove-practice help create-structure install-dep install test-python test

create-practice:
ifndef PRACTICE
	$(error must pass val PRACTICE)
endif
	@echo "Creating practice: $(PRACTICE)"
	mkdir -p $(PRACTICE)
	cp PracticeMakefile $(PRACTICE)/Makefile
	@echo "Practice $(PRACTICE) created successfully!"
	@echo ""
	@echo "Initializing project structure inside $(PRACTICE)..."
	cd $(PRACTICE) && make init
	@echo ""
	@echo "========================================="
	@echo "Practice $(PRACTICE) is ready!"
	@echo "To work with it, run: cd $(PRACTICE)"
	@echo "Then run 'make help' to see available commands"
	@echo "========================================="

remove-practice:
ifndef PRACTICE
	$(error must pass val PRACTICE)
endif
	@echo "Removing practice: $(PRACTICE)"
	rm -rf $(PRACTICE)
	@echo "Practice $(PRACTICE) removed successfully!"

help:
	@echo "This makefile for repo.level activity"
	@echo ""
	@echo "Available commands:"
	@echo "  make create-practice PRACTICE=<name>  - Create new practice directory with full structure"
	@echo "  make remove-practice PRACTICE=<name>  - Remove practice directory"
	@echo "  make create-structure                 - Create project structure in current directory"
	@echo "  make install-dep                      - Install dependencies"
	@echo "  make install                          - Install package in dev mode"
	@echo "  make test-python                      - Run pytest"
	@echo "  make test                             - Install deps and run tests"

create-structure:
	@echo "Creating project structure..."
	mkdir -p src tests docs
	touch README.md setup.py requirements.txt
	touch docs/DOMAIN.md
	touch src/.gitkeep tests/.gitkeep
	@echo "Project structure created successfully!"

install-dep:
	pip install -r requirements.txt

install:
	pip install -e .

test-python:
	python3 -m pytest -v

test: install-dep install test-python
