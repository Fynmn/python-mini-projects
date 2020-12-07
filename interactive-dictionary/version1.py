import json
import difflib

data = json.load(open("data.json"))

def word_match():
    probabilityMatch = []
    matched = difflib.get_close_matches(word, data.keys())
    
    for match in matched:
        val = difflib.SequenceMatcher(None, word, match).ratio()
        probabilityMatch.append(val)
        indexOfMatch = probabilityMatch.index(max(probabilityMatch))
        
    return matched[indexOfMatch]

def translate(wordToTranslate):
    wordToTranslate.lower()
    translatedWord = word_match()
    if wordToTranslate in data.keys():
        searchWord(wordToTranslate)
        return ""
    else:
        ans = input("Do you mean {}(y/n)? ".format(translatedWord)).lower()
        if ans == 'y':
            searchWord(translatedWord)
        elif ans == 'n':
            exit()
        else:
            print("Invalid input. Try again. ")
        return ""

def searchWord(wordToSearch):
    print(wordToSearch.upper())
    for i in range(len(data[wordToSearch])):
        print("- " + data[wordToSearch][i])
    

while True:
    word = input("Enter word: ")

    print(translate(word))
    
    answer = input("Do you want to continue(y/n)? ").lower()
    if answer == 'y':
        pass
    elif answer == 'n':
        exit()
    else:
        print("Please neter a valid input.")
