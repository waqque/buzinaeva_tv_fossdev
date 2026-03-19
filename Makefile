help:
	@echo "This makefile for repo-level activity"
	ifndef $(PRACTICE)
	mkdir -p $(PRACTICE)
create-practice:
	mkdir demo-practice

remove-practice:
	rm -rf $(PRACTICE)


mkdir demo-practice
mkdir demo-practice/src
mkdir demo-practice/tests
mkdir demo-practice/docs
mkdir demo-practice/README.md 
