#!/bin/bash
argsterminal=""
for arg in "$@"; do
    argsterminal="$argsterminal $arg"
done
python3 ~/.linguax/executar.py $argsterminal
