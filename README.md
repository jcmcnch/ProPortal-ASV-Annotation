# ProPortal-ASV-Annotation

This repository contains a BLAST database from [ProPortal](https://img.jgi.doe.gov/cgi-bin/proportal/main.cgi) that allows a user to assign ecotype-level taxonomy to *Cyanobiaceae* ASVs.

Here's how it works:

- Your ASV queries are BLASTed against a database of full-length *Prochlorococcus* and *Synechococcus* 16S rRNA obtained from **ProPortal** genome assemblies (using [barrnap](https://github.com/tseemann/barrnap)), requiring **100% nucleotide identity and 100% coverage**.
- A python script then parses the results to generate ecotype-level classifications. It will also tell you if the classification is ambiguous - i.e. there are perfect matches to more than one clade or genus.

Some example results are included here from the GP13 and GA03 BioGEOTRACES cruises.

Important notes:

- Only set up to work for ASVs - may give spurious results for OTUs since centroids may not represent the true biological sequence.

Setup:

- Conda environments are specified in `env/`
- Unless you want to recreate or modify the database, you can just put an input fasta file in `ASVs-2-classify` and run the following scripts:

```
#will BLAST everything in the ASVs-2-classify folder
./scripts/07-blast-all-datasets.sh

#script requires BLAST results as sys.argv[1] (i.e. second argument after python script)
./scripts/08-classify-ASVs-with-ProPortal.py blast-results/220123.Synechococcales.GA03.blastout.tsv > ProPortalReclassification/220124.GA03.results.tsv
```
