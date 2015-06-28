#!/bin/bash

echo "Problem # | Time (ms)" > timings.txt
echo "----------+----------" >> timings.txt

for p in $(ls -1 solutions | grep "^p"); do
    t=$(python solutions/$p | grep Time | cut -f 2 -d " ")
    ts=$(printf "%8.2f" ${t#0})
    pn=$(echo $p | cut -c 2-4)
    echo "$pn       | $ts" >> timings.txt
    echo "$pn" 1>&2
done

