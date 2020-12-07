import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        ans = input("Do you mean {}(y/n)? ".format(get_close_matches(word, data.keys(), cutoff=0.8)[0])).lower()
        if ans == 'y':
            w = data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
            return w
        elif ans == 'n':
            print("Word doesn't exist. Please double check it.")
        else:
            print("We didn't understand your entry.")
    else:
        print("The word doesn't exist. Please double check it.")
    
word = input("Enter word: ")
output = translate(word)

for item in output:
    print(item)
