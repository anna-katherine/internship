#!/usr/bin/env bash

main(){
  acronym=""

  for word in $(echo "$1" | tr -d  "*_" | tr "-" " ")
  do
    acronym+="{word:0:1}"
  done

  echo ${acronym^^}
}

main "$@"
