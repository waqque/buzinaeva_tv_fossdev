.PHONY: task1 task2 task3 task4 task5 clean-all

task1:
	cd task1-env && make run

task2:
	cd task2-deps && make check

task3:
	cd task3-types && make check

task4:
	cd task4-style && make format && make lint

task5:
	cd task5-compose && make check

clean-all:
	cd task1-env && make clean || true
	cd task2-deps && make clean || true
	cd task3-types && make clean || true
	cd task4-style && make clean || true
	cd task5-compose && make clean || true