#!/bin/sh

for pensvm in pensvms/*
do
    echo "$pensvm"
    qajson=$(python3 extract.py --pensvmType="$pensvm")
    for json in $qajson
    do
        for style in prompts/*/*
        do
            output="quizType$(echo "${pensvm}" | rev | cut -c1)"
            echo "Output is:" $output
            echo "Prompt Style is:" $style
            echo "Json is:" $json
            python3 promptmatching.py --question_input_path="$json" --prompt_input_path="$style" --output_folder="$output" &
        done
    done
done

