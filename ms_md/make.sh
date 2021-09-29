#!/bin/bash

python papermate.py \
--input manuscript.md \
--csl bib/vancouver-author-date.csl \
--bib bib/refs.bib

#generate a marked-up PDF
#git add, git commit
#git tag -a v3_submitted_version -m "Version for submission"
##git add, git commit
#git tag -a v4_revised -m "Revised version for submission"
#python papermate.py --tags v4_revised v3_submitted

#generate .docx
#python papermate.py --docx

#generate tex
#python papermate.py --tex
