#!/usr/bin/env python3

#NOTE: Script assumes that blastoutput in outfmt 6 (tab-separated) and has not been sorted or otherwise manipulated

import csv
import sys
import re

#parse blast results
ASVid=''
classification=''
aClass=[]
for astrLine in csv.reader(open(sys.argv[1]), csv.excel_tab):
    
    #set ASVid by column 1 (query sequence)
    if astrLine[0].strip() != ASVid:
        
        #print results from previous ASV
        uniqueMatches = set(aClass)
        aUniqueMatches = list(uniqueMatches)
        if len(aUniqueMatches) == 1:
            print('\t'.join([ASVid, aUniqueMatches[0]]))
        if len(aUniqueMatches) > 1:
            if ( len(list(filter(lambda x:'Synechococcus' in x, aUniqueMatches))) > 0 ) and ( len(list(filter(lambda x:'Prochlorococcus' in x, aUniqueMatches))) > 0 ):
                classString = "Unclassified Cyanobiaceae with non-unique perfect matches to " + " and ".join(list(uniqueMatches))
                print('\t'.join([ASVid, classString]))
            else:
                classString = list(uniqueMatches)[0].split("-")[0].split("_")[0]  + " with non-unique perfect matches to " + " and ".join(list(uniqueMatches))
                print('\t'.join([ASVid, classString]))
        
        #clear classification array for each new ASV
        aClass = []
        
        #set new ASV id
        ASVid=astrLine[0].strip()

    #check for Syn IDs that start with "5"
    if re.match('^5', astrLine[1].strip()):
        classification = "Synechococcus_" + '.'.join(astrLine[1].strip().split(".")[0:2])
    elif re.match('^CDR', astrLine[1].strip()):
        classification = "Synechococcus_" + astrLine[1].strip().split(".")[0]
    elif re.match('^Prochlorococcus', astrLine[1].strip()):
        classification = astrLine[1].strip().split(".")[0]
    else:
        classification = "Prochlorococcus_" + astrLine[1].strip().split(".")[0]

    #add classification to a tuple that takes only unique values
    aClass.append(classification)

#print results from last ASV
uniqueMatches = set(aClass)
aUniqueMatches = list(uniqueMatches)
if len(aUniqueMatches) == 1:
    print('\t'.join([ASVid, aUniqueMatches[0]]))
if len(aUniqueMatches) > 1:
    if ( len(list(filter(lambda x:'Synechococcus' in x, aUniqueMatches))) > 0 ) and ( len(list(filter(lambda x:'Prochlorococcus' in x, aUniqueMatches))) > 0 ):
        classString = "Unclassified Cyanobiaceae with non-unique perfect matches to " + " and ".join(list(uniqueMatches))
        print('\t'.join([ASVid, classString]))
    else:
        classString = list(uniqueMatches)[0].split("-")[0].split("_")[0]  + " with non-unique perfect matches to " + " and ".join(list(uniqueMatches))
        print('\t'.join([ASVid, classString]))
