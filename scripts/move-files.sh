#!/bin/bash
while read line ; do 

	outdir=`echo $line | cut -f2- -d" " | sed -E 's/ |\//-/g'`
	folder=IMG_`echo $line | cut -f1 -d" "`
 	mv input-IMG-ids/$folder $outdir

done < 220121_ProPortal_genome-clade-matching.tsv
