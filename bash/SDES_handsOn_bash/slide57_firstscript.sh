#!/bin/bash
mkdir ~/$1
cut -d " " -f 2- marks1.txt  | paste -d " " students.txt - \
 | sort > ~/marks/marks.txt
