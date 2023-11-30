#!/bin/bash

repertoire=$1

help(){
    echo "Syntaxe: ./main.sh path/to/repetoire"
    echo "-h ou --help pour afficher l'aide"
    exit 1
}

if [ "$1" == "-h" ] || [ "$1" == "--help" ] ; then
    help
    exit 0
fi

python3 parcourir.py $repertoire