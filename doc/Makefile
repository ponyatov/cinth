TEX = manual.tex header.tex

LATEX = pdflatex -halt-on-error

manual.pdf: $(TEX) Makefile
	$(LATEX) $^ && $(LATEX) $^
