all: doc/manual.pdf

run: cinth.py 
	python $^

doc/manual.pdf: doc/Makefile doc/*.tex
	$(MAKE) -C doc
