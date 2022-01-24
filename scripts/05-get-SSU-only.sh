#!/bin/bash

mkdir -p found-rRNA-SSU-only

for item in `ls found-rRNA/*fna`; do

	outfile=`basename $item .fna`.SSU.fna

	awk 'BEGIN {RS=">"} /16S_rRNA|18S_rRNA/ {print ">"$0}' $item | grep "\S" > found-rRNA-SSU-only/$outfile

done

#remove empty files
find ./found-rRNA-SSU-only -size  0 -print0 | xargs -0 rm --
