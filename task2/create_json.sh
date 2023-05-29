#!/bin/sh

for pensvm in /home/Sophia.Huang.24/modulus-magnus-linguae/task2/pensvms/*
do
    echo "$pensvm"
    pensvmName=$(basename "$pensvm")
    python3 ~/modulus-magnus-linguae/task2/extract.py --pensvmType="$pensvm" &
done

