all: docs/index.html

run: cinth.py 
	python $^

doc/manual.pdf: doc/Makefile doc/*.tex
	$(MAKE) -C doc

CWD  = $(CURDIR)
DOCS = $(CWD)/docs
docs/index.html: doc/*.tex
	rm -rf $(DOCS) ; mkdir $(DOCS)
	cd doc ; latex2html -dir $(DOCS) manual