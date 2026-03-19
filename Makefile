help:
	@echo "This makefile for repo-level activity"
	mkdir -p $(PRACTICE)
create-practice:
ifndef $(PRACTICE)
	$(error must pass val via PRACTICE)
endif
	@echo "Crearing"
	mkdir -p $(PRACTICE)

remove-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif
	rm -rf $(PRACTICE)


mkdir demo-practice
mkdir demo-practice/src
mkdir demo-practice/tests
mkdir demo-practice/docs
mkdir demo-practice/README.md 
