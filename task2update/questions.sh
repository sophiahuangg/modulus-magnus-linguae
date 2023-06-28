#!/bin/sh

total=0

for quiz in quizstyle/*/*
do
    qPerSection=$(jq length "$quiz")
    total=$((total+qPerSection))
done

echo "Total number of questions is: $total"
