import numpy as np

fn = r"COSC3306_FA2026_Assignment_1_string_Team_2.txt"
with open(fn) as f:
    s0 = f.read()

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


words_fn = r"google-10000-english-usa-no-swears-short-medium.txt"
with open(words_fn) as f:
    words = f.read().splitlines()


valid_words = set()


for i in range(20):
    s1 = recursiveScrabble(s0)
    substrs = [s1[i:j] for i in range(len(s1)) for j in range(i + 1, len(s1) + 1) if j - i > 3 and j - i < 7]
    for substr in substrs:
        if substr in words:
            valid_words.add(substr)


valid_words_dict = {}
for word in valid_words:
    valid_words_dict.setdefault(len(word), []).append(word)

print("Valid words found:")
for word in valid_words_dict:
    print(f"{word}: {valid_words_dict[word]}")

