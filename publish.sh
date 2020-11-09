#!/bin/bash

# Script for updating website

source activate pelican
read -p "Enter your git commit comment : " comment
pelican content -o output -s publishconf.py

ghp-import -m "$comment" -c gregpawin.com --no-jekyll -b master output

git push -f origin master
git add content
git commit -m "$comment"
git push -f origin content

#cp ~/Documents/Website/favicon_io/* ~/Documents/Website/gregpawin.github.io/output
#cd output
#git add android-chrome-192x192.png favicon-16x16.png site.webmanifest android-chrome-512x512.png favicon-32x32.png
#apple-touch-icon.png favicon.ico
#git commit -m "$comment"
#git push -f origin master
