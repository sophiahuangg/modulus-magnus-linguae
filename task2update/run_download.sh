#!/bin/bash

# Looping through all chapters of https://exercitia-latina.surge.sh/ and extracting the html content

url="https://exercitia-latina.surge.sh/chapters"

content=$(curl -s "$url")
echo $content

# Checking to see where in the HTML the chapters are stored
echo $chapters

# Retrieving the urls of each chapter and downloading content of each
for chapter in $chapters
do
    echo $chapter
    ch_url="https://exercitia-latina.surge.sh$chapter"
    wget "$ch_url"
done
