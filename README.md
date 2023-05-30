# Week 1 Tasks

## Part 1: What is the right way to prompt the language models?

```
Q: This is a ~
A: test

Q Hello ~
A: world

Q: ~ world
A: [answer]
```

Another way of prompting

```
This is a quiz of your ability to understand latin grammar. For each problem there is a ~ character in the text and your job is to figure out what word should be replaced by the ~

Q: This is a ~
A: [answer]
```

## Part 2: Given a machine formatted quiz, write a LMQL script for that quiz.

### Part 2a: In order to complete part 2, standard json format of how a question should be formatted.

```
{ 'text': 'Hello ~.', 'answer': 'world'}
```

parse the original source into the JSON format.

### Part 2aa: manually generate some json questions to work with on part 2b.

### Part 2b: Given a JSON format above, generate the LMQL code from part 1. Generates all possible prompt designs.

## Part 3: Extract the answers from the model and compare them to the ground truth. Output a score of how many questions were correct and incorrect.


