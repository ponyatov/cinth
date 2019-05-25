all: doc/manual.pdf

run: cinth.py 
	python $^

doc/manual.pdf: doc/Makefile doc/*.tex doc/*.py
	$(MAKE) -C doc
