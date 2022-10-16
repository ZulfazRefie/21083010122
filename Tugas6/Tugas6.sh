#!/bin/bash

echo -n "Input : "
read n

declare -a ni

i=0
while [ $i -lt $n ]
do
    read a[$i]
    ni[$i]=${a[$i]}
    i=`expr $i + 1`
done

x=0
for v in ${ni[@]}
do
    let x+=$v
done

echo " "
echo "IPS mhs = $x / $n"
echo "IPK mhs = $((x / n))"
