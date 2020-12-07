import json
from difflib import get_close_matches

data = json.load(open('data.json'))
x = True

def translate(word):
    if word in data:
        print(word.upper())
        for i in range(len(data[word])):
            print('- ' + data[word][i])
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        ans = input("Do you mean {}(y/n)? ".format(word)).lower()
        if ans == 'y':
            print(word.upper())
            w = data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
            for i in w:
                print('- ' + i)
        elif ans == 'n':
            print("Word doesn't exist. Please double check it.")
        else:
            print("We didn't understand your entry.")
    else:
        print("The word doesn't exist. Please double check it.")
    
while x:
    word = input("\nEnter word: ").lower()
    translate(word)
    answer = input('\nDo you want to continue(y/n)? ').lower()
    if answer == 'y':
        x
    elif answer =='n':
        x = False
    else:
        print("We don't recognize your response. Please enter a new word.")
