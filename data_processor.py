import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def get_definition(word):
    if word.lower() in data:
        return data[word.lower()]
    elif len(get_close_matches(word, data.keys())) > 0:
        response = input ("Did you mean %s instead? Y/N: " % get_close_matches(word, data.keys())[0])
        if response == "Y" or response == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif response == "N" or response == "n":
            return "The word doesn't exist. Please check and try again"
        else:
            return "We didn't understand the response"
    else:
        return "Cannot find word definition"


word = input("Enter a word to get definition: ")

output = get_definition(word)

if type(output) == list:
    for result in output:
        print(result)
else:
    print(output)


