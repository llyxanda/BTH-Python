#!/usr/bin/env bash
cd me/tentamen/ || exit
e() { exit; }; export -f e
f() { exit 1; }; export -f f

echo "Run correct script"
dbwebb test tentamen

read -p "Press to view code" answer
