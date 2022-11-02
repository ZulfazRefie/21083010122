#!/bin/bash

# Mendeklarasikan fungsi
panjang() {
  echo "Masukkan Panjang : ";
  read x
  echo
}

lebar() {
  echo "Masukkan Lebar : ";
  read y
  echo
}

luas() {
  panjang
  lebar
  let luasp=$((x * y))
  echo "Luas Persegi :"
  echo $luasp
  echo
}

# Memanggil fungsi
luas
