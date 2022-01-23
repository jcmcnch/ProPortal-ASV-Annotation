while read line ; do mkdir -p `echo $line | cut -f2- -d" " | sed -E 's/ |\//-/g'` ; done < 220121_ProPortal_genome-clade-matching.tsv
