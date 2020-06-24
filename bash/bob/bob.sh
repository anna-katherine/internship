#!/usr/bin/env bash

if [[ ${#1} = 0 ]]; then
  echo "Fine. Be that way!"
question=false
mark='?'
yell=false
case $1 in

  *"$mark"*)
    question=true
  ;;
esac

if [[ "$1" == "${1^^} ]]; then
  yell=true
fi

if [[ $question  && $yell ]]
  echo "Calm down, I know what I'm doing!"
elif $question ; then
  echo "Sure."
elif $yell ; then
  echo "Whoa, chill out!"
else
  echo "Whatever."
fi
