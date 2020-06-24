#!/usr/bin/env bash

main () {
    score=0

    declare -A val

    val['a']=1
    val['e']=1
    val['i']=1
    val['o']=1
    val['u']=1
    val['l']=1
    val['n']=1
    val['r']=1
    val['s']=1
    val['t']=1
    val['d']=2
    val['g']=2
    val['b']=3
    val['c']=3
    val['m']=3
    val['p']=3
    val['f']=4
    val['h']=4
    val['v']=4
    val['w']=4
    val['y']=4
    val['k']=5
    val['j']=8
    val['x']=8
    val['q']=10
    val['z']=10

    for char in $(echo "${1,,}" | tr -d " " | grep -o . ); do
        score=$(( "$score" + "${val["$char"]}"))
    done


    echo "$score"
}

main "$@"
