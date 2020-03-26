#!/bin/bash

set -eu

for f in *.py
do
    if [[ "$f" =~ p[0-9][0-9].py ]]; then
        # echo "$f"
        mv "$f" "$(echo "$f" | sed -r -e 's/p([0-9][0-9]).py/p0\1.py/g')"
    elif [[ "$f" =~ p[0-9].py ]]; then
         # echo "$f"
         mv "$f" "$(echo "$f" | sed -r -e 's/p([0-9][0-9]).py/p0\1.py/g')"
    else
        # echo "$f"
        echo "mismatch"
    fi
done
