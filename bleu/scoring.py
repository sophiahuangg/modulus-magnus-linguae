from nltk.translate.bleu_score import sentence_bleu
import json, os, sys

inputjson = sys.argv[1]
bleuscores = []

with open(inputjson, 'r') as f:
    json_data = json.load(f)

for question in range(len(json_data)):
    # reference
    ref = json_data[question][1]['answer']
    reference = [ref.split()]
    # candidate
    can = json_data[question][2]['model_output']
    candidate = can.split()
    # bleu score
    score = sentence_bleu(reference, candidate)

    bleuscore = {
        "question": question,
        "reference": reference,
        "candidate": candidate,
        "score": score
    }
    bleuscores.append(bleuscore)

directory = "scores"
if not os.path.exists(directory):
    os.makedirs(directory)

score_file = os.path.join(directory, os.path.basename(inputjson))
with open(score_file, 'w') as file:
    json.dump(bleuscores, file)
