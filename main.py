import json
from difflib import get_close_matches

file_path = './data/data1.json'
data = [json.loads(line) for line in open(file_path, 'r')]
word_dict = data[0]
word_list = list(word_dict.keys())


def translate(w):
    similar_words = get_close_matches(w, word_list, 3, 0.8)
    if w in word_list:
        print(*word_dict[w], sep='\n')
    elif w.capitalize() in word_list:
        print(*word_dict[w.capitalize()], sep='\n')
    else:
        if len(similar_words) == 0:
            print('Khong tim thay tu vung')
        else:
            print(f'Did you mean: {similar_words}?')
            choice = int(input(f'Enter position of the word, from 1 to {len(similar_words)}: '))
            translate(similar_words[choice-1])


# Get the input from the user
while True:
    word = str(input('Nhap tu can tra: ')).lower()
    translate(word)
    if word == "exit":
        break

