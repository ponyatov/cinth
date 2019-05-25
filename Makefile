all: doc/manual.pdf

run: cinth.py 
	python $^

doc/manual.pdf: doc/Makefile doc/*.tex doc/*.py
	$(MAKE) -C doc

NOW = $(shell date +%d%m%y)
release: doc/manual.pdf
	git tag $(NOW) ; git push --tags gh
	cp $< cinth_$(NOW).pdf
