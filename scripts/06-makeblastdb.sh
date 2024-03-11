#!/bin/bash -i
conda activate blast-env

makeblastdb -dbtype nucl -in blast-db/220123.ProPortal16Sdb.fasta
