#!/bin/bash
lim1=$RANDOM
let "lim1 %= 20"
echo $lim1
for i in `seq 1 "$lim1"`
do 
   lim2=$RANDOM
   let "lim2 %= 30"
   echo $i
   for j in `seq 2 "$lim2"`
   do 
      touch $i.$j 
   done
   echo "Next"
done

