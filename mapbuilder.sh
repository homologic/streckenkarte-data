#!/bin/bash


temp=$(mktemp -d)

mkdir "$temp/data"
for i in data/*
do	
	ogrmerge.py -single -o "$temp/$i.json"  "$i"/* 
done


tippecanoe -aN -z10 -o "$temp/strecken.pmtiles" $temp/data/*.json

mv $temp/strecken.pmtiles /var/www/html/

rm -r $temp
