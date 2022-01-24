#!/bin/bash -i
conda activate blast-env

mkdir -p blast-db

cat found-rRNA-SSU-only/*fna > blast-db/220123.ProPortal16Sdb.fasta

makeblastdb -dbtype nucl -in blast-db/220123.ProPortal16Sdb.fasta
