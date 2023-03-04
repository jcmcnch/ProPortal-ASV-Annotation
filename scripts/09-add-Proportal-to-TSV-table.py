#!/usr/bin/env python3

#import libraries
import sys
import csv

#create empty hash
hashClassifications = {}

#Read in previous ASV-based classifications (e.g. from comparison to ProPortal genomes)
#Format requirements: tab-separated values with following columns (no headers):
#OTU_ID from qiime2 (i.e. hash) 	classification string from ProPortal script
for astrLine in csv.reader(open(sys.argv[1]), csv.excel_tab):
    hashClassifications[astrLine[0]] = astrLine[1]

#Read in a taxonomically-annotated ASV table (tab-separated format)
#that has NOT been classified with model-relevant annotations
#per the idiosyncratic way that I output ASV tables, columns must be as follows:
#OTU_ID	taxonomy	sample1 sample2 ... samplen
#Often the taxonomy is the last column, e.g. if you export from a biom file with taxonomy added as metadata

#will print out a new table with the ProPortal annotations as the third column after the taxonomy

aTaxa = list(hashClassifications.keys())
	
for astrLine in csv.reader(open(sys.argv[2]), csv.excel_tab):
    query = astrLine[0].strip()
    #if ASV id matches
    if query in aTaxa:
        #print replace the 3rd column with the associated classification
        aOut = [astrLine[0], astrLine[1], hashClassifications[query]] + astrLine[3:]
        print('\t'.join(aOut))
    #Add ProPortal header if it's the first line
    elif astrLine[1] == "taxonomy":
        #add column header
        aOut = [astrLine[0], astrLine[1], "ProPortal_Ecotype_Classification"] + astrLine[3:]
        print('\t'.join(aOut))
    #or if the ASV id doesn't match the dictionary
    else:
        #replace the 3rd column an empty field
        aOut = [astrLine[0], astrLine[1], ""] + astrLine[3:]
        print('\t'.join(aOut))
