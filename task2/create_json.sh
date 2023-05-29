#!/bin/sh

for pensvm in pensvms/*
do
    echo "$pensvm"
    pensvmName=$(basename "$pensvm")
    python3 extract.py --pensvmType="$pensvm" &
done

