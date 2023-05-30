import unittest
import os
import json
from extract import extract_q_and_a, create_qa_json

class TestYourFile(unittest.TestCase):
    def test_extract_q_and_a(self):
        text = "ls|Nilus fluvi~ est.|us"
        questions, answers = extract_q_and_a(text)
        self.assertEqual(questions[0], 'Nilus fluvi~ est.')
        self.assertEqual(answers[0], 'us')
        
        text = "lw|Sicilia ~ est.|insula"
        questions, answers = extract_q_and_a(text)
        self.assertEqual(questions[0], 'Sicilia ~ est.')
        self.assertEqual(answers[0], 'insula')

        text = "ll|Ubi est Roma?|Roma in Italia est."
        questions, answers = extract_q_and_a(text)
        self.assertEqual(questions[0], 'Ubi est Roma?')
        self.assertEqual(answers[0], 'Roma in Italia est.')

    def test_create_qa_json(self):
        questions = ['What is Python?']
        answers = ['Python is a programming language.']
        create_qa_json(questions, answers)
        
        with open('qa_pairs.json', 'r') as f:
            data = json.load(f)
        
        self.assertEqual(data['questions'][0]['question'], 'What is Python?')
        self.assertEqual(data['questions'][0]['answer'], 'Python is a programming language.')
        
        # clean up
        os.remove('qa_pairs.json')

if __name__ == '__main__':
    unittest.main()
