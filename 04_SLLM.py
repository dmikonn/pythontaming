import numpy as np

SOURCE_FILE = input("Please, insert the path to the text source file: \n")

with open(SOURCE_FILE, "r") as text_file:
    text = text_file.read()

CORPUS = text.split()

def make_pairs(corpus): # this generator yealds every word pair from the corpus
    for i in range(len(corpus)-1):
        if corpus[i].strip(",.-:").isalpha() and corpus[i+1].strip(",.-:").isalpha():
            yield (corpus[i], corpus[i+1])

pairs = make_pairs(CORPUS)

DECISION_TREE = {}

for word_1, word_2 in pairs: # this cycle populates the main dictionary to make a decision tree out of the corporeal word pairs
    if word_1 in DECISION_TREE.keys():
        DECISION_TREE[word_1].append(word_2)
    else:
        DECISION_TREE[word_1] = [word_2]

FIRST_WORD = np.random.choice(CORPUS)

while FIRST_WORD.islower():
    FIRST_WORD = np.random.choice(CORPUS)

print(FIRST_WORD)

NOVEL = [FIRST_WORD]
NOVEL_LENGTH = 100


for i in range(NOVEL_LENGTH):
    try:
        NOVEL.append(np.random.choice(DECISION_TREE[NOVEL[-1]]))
    except KeyError:
        NOVEL.append(np.random.choice(CORPUS))
while NOVEL[-1].endswith(".") == False: # keeps appending the STORY until it stops with the word with the comma
    try:
        NOVEL.append(np.random.choice(DECISION_TREE[NOVEL[-1]]))
    except KeyError:
        NOVEL.append(np.random.choice(CORPUS))

print(' '.join(NOVEL))
