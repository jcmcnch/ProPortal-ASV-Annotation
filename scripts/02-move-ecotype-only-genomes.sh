#!/bin/bash

mkdir -p genomes-with-proportal-ecotype

while read line ; do 

	mkdir -p genomes-with-proportal-ecotype/HL
	mv Not-Assigned/IMG_$line genomes-with-proportal-ecotype/HL

done < input-info/HL.ids

while read line ; do

        mkdir -p genomes-with-proportal-ecotype/LL
        mv Not-Assigned/IMG_$line genomes-with-proportal-ecotype/LL

done < input-info/LL.ids
