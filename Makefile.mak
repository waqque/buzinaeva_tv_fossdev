.PHONY: create-structure install-dep install test-python test

create-structure:
	mkdir -p $(PRACTICE)/src $(PRACTICE)/tests $(PRACTICE)/docs
	touch $(PRACTICE)/README.md $(PRACTICE)/setup.py $(PRACTICE)/requirements.txt
	touch $(PRACTICE)/docs/DOMAIN.md
	touch $(PRACTICE)/src/.gitkeep $(PRACTICE)/tests/.gitkeep

install-dep:
	pip install -r requirements.txt

install:
	pip install -e .

test-python:
	python3 -m pytest

test: install-dep install test-python