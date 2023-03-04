from random import randint 
import pandas


data = pandas.read_csv("./data/french_words.csv")
dictionary = data.to_dict()
print(dictionary)
LENGTH = len(dictionary["French"])


def get_item(en=-1, fr=-1):
    word = ""
    if en == -1 and fr == -1:
        index = randint(0, LENGTH-1)
        word = dictionary["French"][index]
    elif en != -1:
        for (index, row) in data.iterrows():
            if row["English"] == en:
                ind = index
        word = dictionary["French"][ind]
        
    elif fr != -1:
        for (index, row) in data.iterrows():
            # print(index, row["French"])
            if row["French"] == fr:
                ind = index
        word = dictionary["English"][ind]

    return word
    