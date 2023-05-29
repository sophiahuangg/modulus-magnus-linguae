#!/bin/sh

for pensvm in /home/Sophia.Huang.24/modulus-magnus-linguae/prompts/*
do
    pensvm_folder=$(basename "$pensvm")
    echo "$pensvm_folder"
    for prompt in "$pensvm"/*
    do
        style=$(basename "$prompt")
        echo "The Style is: $style"
        nohup /home/Sophia.Huang.24/modulus-magnus-linguae/task2/extract.py > jsonoutputs/"$pensvm_folder"."$style" &
    done
done
