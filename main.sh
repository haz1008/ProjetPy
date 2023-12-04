#!/bin/bash


help(){
    echo "Syntaxe: ./main.sh path/to/repetoire"
    echo "-h ou --help pour afficher l'aide"
    exit 1
}

if [ "$1" == "-h" ] || [ "$1" == "--help" ] ; then
    help
    exit 0
fi
if [ $# -ne 1 ]; then
    echo "Veuillez saisir un repertoire."
    help
    exit 2 
fi

repertoire=$1

python3 parcourir.py $repertoire