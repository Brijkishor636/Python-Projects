import json
from difflib import get_close_matches

data = json.load(open('Project_2/data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]   
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("You want to write %s instead" %get_close_matches(word, data.keys())[0])
        inp = input("Press y for confirm or n for not :- ")
        if inp == "y" or inp == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif(inp == "n" or inp == "N"):
            return ("Pugger your pow wrong step on keys.")
        else:
            return ("You have entered wrong character, press only y or n")
    else:
        return "The word doesn't exist. Please double check it."

    # inp2 = input("Do you want more word to search y or n")
    # if(inp2 == "Y" or inp2 == "y"):
    #     x = input("Enter the word to search")
    #     translate(x)
    # else: 
    #     return
    
x = input("Enter the word to search : ")
output = translate(x)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

