import numpy as np

# read the input string and seed from the file
fn = r"COSC3306_FA2026_Assignment_1_string_Team_2.txt"
with open(fn) as f:
    s0 = f.read()

# split the input string into the string and seed
s0 = s0.split()
seed = int(s0[1])
s0 = s0[0]

np.random.seed(seed)

def recursiveScrabble(s0):
    if len(s0) <= 1:
        return s0
    length = len(s0)
    mid = length // 2
    left = recursiveScrabble(s0[:mid])
    right = recursiveScrabble(s0[mid:])

    if np.random.random() < 0.5:
        return right + left
    else:
        return left + right

def determine_valid_scrabbled_words(s0, words,iterations=20):
    valid_words = set()
    for i in range(iterations):
        s1 = recursiveScrabble(s0)
        substrs = [s1[i:j] for i in range(len(s1)) for j in range(i + 1, len(s1) + 1) if j - i > 3 and j - i < 7]
        for substr in substrs:
            if substr in words:
                valid_words.add(substr)
    return sorted(valid_words)


words_fn = r"google-10000-english-usa-no-swears-short-medium.txt"
with open(words_fn) as f:
    words = f.read().splitlines()

valid_words = determine_valid_scrabbled_words(s0, words)

valid_words_dict = {}
for word in valid_words:
    valid_words_dict.setdefault(len(word), []).append(word)

for length in sorted(valid_words_dict.keys()):
    print(f"Length {length}: {', '.join(valid_words_dict[length])}")
