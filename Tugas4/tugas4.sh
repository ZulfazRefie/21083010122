#!/bin/bash

echo -n "Masukkan angka ganjil: ";
read i

while [ $i -ge 1 ];
do
  echo "$i";
  let i=$i-2
done
