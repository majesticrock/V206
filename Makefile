all: build/main.pdf

# hier Python-Skripte:
build/plot-t-T.pdf: plot-t-T.py matplotlibrc header-matplotlib.tex csv/zeit-temperatur.csv | build
	TEXINPUTS=$$(pwd): python plot-t-T.py

build/plot-T-p1.pdf: plot-T-p1.py matplotlibrc header-matplotlib.tex csv/temperatur-druck1.csv | build
	TEXINPUTS=$$(pwd): python plot-T-p1.py

build/plot-T-p2.pdf: plot-T-p2.py matplotlibrc header-matplotlib.tex csv/temperatur-druck2.csv | build
	TEXINPUTS=$$(pwd): python plot-T-p2.py

build/plot-t-P.pdf: plot-t-P.py matplotlibrc header-matplotlib.tex csv/zeit-leistung.csv | build
	TEXINPUTS=$$(pwd): python plot-t-P.py

build/plot-L.pdf: l_plot.py matplotlibrc header-matplotlib.tex csv/tempbar.csv | build
	TEXINPUTS=$$(pwd): python l_plot.py
# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: content/temp-druck.tex content/zeit-temp.tex content/zeit-leistung.tex content/temppascal.tex build/plot-t-T.pdf build/plot-T-p1.pdf build/plot-T-p2.pdf build/plot-t-P.pdf build/plot-L.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
