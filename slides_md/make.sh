#!/bin/bash

# Synaptics install pandoc, texlive-xetex
pandoc slides.md \ 
--pdf-engine=xelatex \ 
--citeproc \ 
--wrap=preserve \ 
--bibliography=ref.bib \ 
--dpi=300 \ 
from=markdown+escaped_line_breaks \ 
-t beamer -o slides.pdf
