#!/bin/bash

for i in 1 2 3 4 5
do
   var="./dummy.out input${i}file.txt  output$i.txt"
   echo $var
   eval $var
done
