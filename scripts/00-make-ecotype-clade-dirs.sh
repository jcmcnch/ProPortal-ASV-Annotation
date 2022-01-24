while read line ; do mkdir -p genomes-with-ecotypes/`echo $line | cut -f2- -d" " | sed -E 's/ |\//-/g'` ; done < input-info/220121_ProPortal_genome-clade-matching.tsv
