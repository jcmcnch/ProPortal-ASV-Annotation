#!/bin/bash -i
conda activate barrnap-env
mkdir -p found-rRNA

for assembly in `ls genomes-with-proportal-ecotype/*/*/Assembly/IMG_Data/*fna | grep -E "contigs.fna|assembled.fna"`; do

	outdir=`dirname $assembly`
	ecotype=`echo $outdir | cut -f2 -d\/`
	IMGgenomeID=`echo $outdir | cut -f3 -d\/`
	outname=Prochlorococcus-$ecotype-unclassified.$IMGgenomeID.`basename $assembly .fna`.rRNA.fna
	barrnap --kingdom bac --threads 3 --outseq $outdir/$outname $assembly
	cp $outdir/$outname found-rRNA

done
