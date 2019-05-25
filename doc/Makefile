TEX  = manual.tex header.tex
TEX += intro.tex
TEX += frame.tex io.tex meta.tex

LATEX = pdflatex -halt-on-error

manual.pdf: $(TEX) Makefile
	$(LATEX) $^ && $(LATEX) $^
