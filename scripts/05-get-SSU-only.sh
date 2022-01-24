#!/bin/bash

mkdir -p found-rRNA-SSU-only

for item in `ls found-rRNA/*fna`; do

	outfile=`basename $item .fna`.SSU.fna

	awk 'BEGIN {RS=">"} /16S_rRNA|18S_rRNA/ {print ">"$0}' $item | grep "\S" > found-rRNA-SSU-only/$outfile

done

#remove empty files
find ./found-rRNA-SSU-only -size  0 -print0 | xargs -0 rm --

#replace fasta headers with ecotype info so BLAST results can be parsed visually
for item in found-rRNA-SSU-only/*fna ; do 
	
	replacementString=`basename $item .fna | cut -f1,2 -d_ | sed 's/.assembled.rRNA.SSU//g'`
	sed -i "s/>16S_rRNA/>$replacementString::16S_rRNA/" $item

done
