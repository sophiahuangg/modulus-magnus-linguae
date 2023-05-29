#!/usr/bin/env python

import json, re, argparse, os

def extract_q_and_a(text):
    question_answer_pattern = r'\|(.*)\|(.*)'
# Regex patterns to find questions and answers
    matches = re.findall(question_answer_pattern, text)
    questions = [match[0] for match in matches]
    answers = [match[1] for match in matches]
    return questions, answers

def create_qa_json(questions, answers, pensvmType):
    filename = os.path.join("jsonoutputs", "pensvm" + pensvmType[-1], pensvmType + ".json")
    print("pensvmType=", pensvmType)
    qa_pairs = [{"question": q, "answer": a} for q, a in zip(questions, answers)]
# Creates a dictionary with key "questions" and value as the list of qa_pairs
    dict_to_dump = {"questions": qa_pairs}

    with open(filename, 'w') as f:
        json.dump(dict_to_dump, f) 
# Dumps the newly created dictionary instead of qa_pairs

def main(pensvmType):
    with open(pensvmType, 'r') as f:
        text = f.read()

    questions, answers = extract_q_and_a(text)
    create_qa_json(questions, answers, os.path.basename(pensvmType))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--pensvmType')
    args = parser.parse_args()

    main(args.pensvmType)
