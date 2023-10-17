#!/bin/bash -i
conda activate vsearch-env

mkdir -p found-rRNA-SSU-QC
outdir=found-rRNA-SSU-QC

for item in `ls found-rRNA-SSU-only/*fna` ; do 

	outfile=`basename $item .fna`.classified.SILVA138.1.tsv
	echo vsearch --sintax $item \
	       	--db /home/db/VSEARCH/220830_SILVA138.1_VSEARCH-formatted.udb \
	        --tabbedout $outdir/$outfile --threads 10 --sintax_cutoff 0 \
		--top_hits_only --topn 1 --notrunclabels

done
