#!/bin/bash
clear

email="me@gmail.com"
pass="secret"

read -p "Email : " logmail
read -sp "Password : " logpass
echo

if [ $email == $logmail ] && [ $pass == $logpass ]
then
  echo "Login sukses"
else 
  echo "Email atau password salah"
fi
