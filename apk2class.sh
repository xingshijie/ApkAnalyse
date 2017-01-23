#!/usr/bin/env bash

PRGDIR=`dirname "$1"`
filename=$(basename "$1")
extension="${filename##*.}"
filename="${filename%.*}"
destDir="$PRGDIR/$filename"

unzip $1 -d ${destDir}
#"/Users/word/AndroidStudioProjects/dexReader/dex2jar-2.0/d2j-dex2jar.sh"  "${destDir}/classes.dex" -o "${destDir}/classes.zip"
#unzip "${destDir}/classes.zip" -d ${destDir}

for file in ${destDir}/*.dex; do
    zipfilename=$(basename ${file})
    zipfilename="${zipfilename%.*}"
    "dex2jar-2.0/d2j-dex2jar.sh"  "${destDir}/${zipfilename}.dex" -o "${destDir}/${zipfilename}.zip"
    unzip -o "${destDir}/${zipfilename}.zip" -d ${destDir}
done