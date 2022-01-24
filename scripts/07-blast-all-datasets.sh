#!/bin/bash -i
conda activate blast-env

mkdir -p blast-results

db=blast-db/220123.ProPortal16Sdb.fasta

for item in ASVs-2-classify/*fasta ; do

	outname=blast-results/`basename $item .fasta`.blastout.tsv

	blastn -query $item -db $db -outfmt 6 -perc_identity 100 -qcov_hsp_perc 100 > $outname

done
