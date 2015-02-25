#!bin/bash
a=0;for i in `less test.txt`;do ((a++)); echo $a:$i; done

