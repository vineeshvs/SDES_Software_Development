#!bin/bash
a=0;
for i in `less $1`; do ((a++)); if [ $a -gt 9 ]; then if [ $a -lt 21 ] then echo $i;fi; fi; done

