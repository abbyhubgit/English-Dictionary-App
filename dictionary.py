import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
# save dictionary json file to python dict 
data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    # for words such as Paris, Texas, etc. 
    elif word.title() in data:
        return data[word.title()]
    # for words such as USA, NATO, etc
    elif word.upper() in data:
        return data[word.upper()]
    else: 
        # words similar to input 
        ls = get_close_matches(word, data.keys(), cutoff = 0.8)

        # no words are similar
        if(ls == []):
            return ["This word doesn't exist. "]

        if(ls != []):
            possible_word = ls[0]
            # suggest the best guess 
            while True: 
                answer = input("Do you mean {}?, y or n: ".format(possible_word)).lower()
                if answer == "n":
                    return ["This word doesn't exist. "]
                elif answer == "y": 
                    return data[possible_word];
                else:
                    return ["Invalid answer"]


# Take user input and translate 
word = input("Enter a word: ")
output = translate(word)
for op in output:
    print(op)