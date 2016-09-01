#!/bin/bash

#Parses data from nfoic.org in an incredibly hacky, but quick one-time way. 
#Creates an imperfect csv file which is very useful for grep/awk.
#Information is then put into a spreadsheet at for future tracking work:

#https://docs.google.com/spreadsheets/d/16HiOEZehb_YoUtCgLKG89oMVO0rLX8nwMevHigv5Lq8

for l in `cat links` ; do wget $l ; done

for state in `ls -1 *resources` ; do
     outfile=`echo $state | awk -F'-' '{print $1$2}'`
     cat $state | egrep -v "CONSTITUTION OF THE STATE OF|QUICK FOI" |\
         tr '\n' ' ' |\
         sed 's/PUBLICATIONS<\/h3>.*//' |\
         sed -r 's/<strong>/\n"/g' |\
         sed 's/PUBLICATION.*//g' |\
         sed 's/<\/strong>//g' |\
         sed -r 's/<br *\/>/","/g' |\
         sed -r 's/"[ \t]+/"/g' |\
         sed 's/<a href="#top.*//' |\
         sed -r 's/<*a href=.[^@]+[^>]+>([^@]+@[^<]+)<\/a>/\1/' |\
         sed -r 's/<\/*(div|font|img|h[1-3]|a name|p)[^>]*>/","/g' |\
         sed -r 's/[ \t]+/ /g' |\
         sed -r "s/<href=\"([^\"]+)\"/<href='\1'/g" |\
         sed -r 's/([^"]| *)$/"/g' |\
         sed 's/ <a/","<a/' |\
         sed -r 's/("," )+/","/g' |\
         grep ^\" |\
         tr '[:upper:]' '[:lower:]'\
     > $outfile
 done
