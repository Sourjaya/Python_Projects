import json
from difflib import get_close_matches
data=json.load(open("data.json"))
def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        ans=input("Did you mean %s instead? Enter Y if yes, or N if no:" % get_close_matches(w,data.keys())[0])
        if ans=="Y" or ans=="y":
            return data[get_close_matches(w,data.keys())[0]]
        elif ans=="N" or ans=="n":
            return "The word doesn't exist.Please check before searching."
        else:
            return "We did not understand your query."
    else:
        return "The word doesn't exist.Please check before searching."
out=input("Do you want to search the dictionary(Y/N):")
if out=="Y" or out=="y":
    while out=="Y" or out=="y":
        word=input("Enter word: ")
        print("-"*30)
        print(" "*30)
        output = translate(word)
        if type(output) == list:
            for item in output:
                print(item)
        else:
            print(output)
        print("-"*30)
        print(" "*30)
        out=input("Do you want to search for other words in the dictionary(Y/N):")