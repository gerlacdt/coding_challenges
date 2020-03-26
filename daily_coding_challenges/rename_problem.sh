#!/bin/bash

set -eu

for f in *.py
do
    if [[ "$f" =~ "problem" ]]; then
        mv "$f" "$(echo "$f" | sed s/problem/p/g)"
    else
        echo "$f"
    fi
done
