TEX  = manual.tex header.tex
TEX += intro.tex
TEX += frame.tex io.tex meta.tex

SRC = *.py

LATEX = pdflatex -halt-on-error

manual.pdf: $(TEX) $(SRC) Makefile
	$(LATEX) $^ && $(LATEX) $^
