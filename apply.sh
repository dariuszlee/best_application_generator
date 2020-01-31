#!/usr/bin/env bash
company=$1
hirer=$2

python3 coverletter.py -c "$company" -i "$hirer" -p | pandoc -o ./generated/coverletter_$company.pdf && pdfunite ./generatedcoverletter_$company.pdf jan2020-resume.pdf ./generated/application_$company.pdf

