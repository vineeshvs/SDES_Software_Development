#!/bin/sh
   lynx -dump "http://www.google.com/search?hl=en&q=$1" |  grep -E "About ([0-9]+,)*[0-9]+ results" | tr -s " " | cut -d" " -f4 

