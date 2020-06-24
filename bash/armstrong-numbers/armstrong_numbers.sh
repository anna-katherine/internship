#!/usr/bin/env bash

sum=0
digit=0
var=$1
place=${#var}
while (($var >0)); do
  let digit=$var%10
  let sum=$sum+$digit**$place
  let var=$var/10
done
if (( "$sum" == $1 )); then
  echo "true"
else
  echo "false"
fi



