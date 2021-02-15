#!/bin/bash

# Synaptics install pandoc, texlive-xetex
pandoc slides.md --pdf-engine=xelatex --citeproc --wrap=preserve --bibliography=ref.bib from=markdown+escaped_line_breaks --dpi=300 -t beamer -o slides.pdf
