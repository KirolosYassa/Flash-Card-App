import json
from random import randint, choice
import pandas


LENGTH = 0
words_to_learn = []

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
    words_to_learn = data.to_dict(orient="records")
    LENGTH = len(words_to_learn)
    if LENGTH <= 1:
        raise FileNotFoundError
    print("Continue with my old data")
except FileNotFoundError:

    data = pandas.read_csv("./data/french_words.csv")
    dictionary = data.to_dict()
    # print(dictionary)
    LENGTH = len(dictionary["French"])
    words_to_learn = data.to_dict(orient="records")
    print("Build new file")

except pandas.errors.EmptyDataError:

    data = pandas.read_csv("./data/french_words.csv")
    dictionary = data.to_dict()
    # print(dictionary)
    LENGTH = len(dictionary["French"])
    words_to_learn = data.to_dict(orient="records")
    print("Empty Error")


print(words_to_learn)


def get_item(en=-1, fr=-1):
    global LENGTH, words_to_learn
    print(f"len(words_to_learn) = {len(words_to_learn)}")
    if len(words_to_learn) <= 2:
        data = pandas.read_csv("./data/french_words.csv")
        dictionary = data.to_dict()
        # print(dictionary)
        LENGTH = len(dictionary["French"])
        words_to_learn = data.to_dict(orient="records")
        print("Build new words to learn data")
        new_data = pandas.DataFrame(words_to_learn)
        new_data.to_csv("./data/words_to_learn.csv", index=False)
        return choice(words_to_learn)

    # try:
    # print(words_to_learn)
    card = choice(words_to_learn)
    # print(f"The Choice Card is = {card}")
    # except IndexError:
        # data = pandas.read_csv("./data/french_words.csv")
        # dictionary = data.to_dict()
        # # print(dictionary)
        # LENGTH = len(dictionary["French"])
        # words_to_learn = data.to_dict(orient="records")
        # print("Index Error Build new words to learn data")

    return card

# def item_found(word):
#     notFound = True
#     for item in words_to_learn:
#         if item["French"] == word:
#             print("Found")
#             return True
#     if notFound:
#         print("Not Found")


def run():
    for (index, row) in dictionary:
        print(index, row["English"])

# print(get_item())
