import random


def main():
    quantity_1 = 1
    quantity_2 = 2
    tense = ["past", "present", "future"]
    counter = 0
    sentences = [1, 2, 3]
    for i in sentences:
        determiner = get_determiner(quantity_1)
        noun = get_noun(quantity_1)
        verb = get_verb(quantity_1, tense[counter])
        prep_phrase = get_prepositional_phrase(quantity_1)
        sentence = (f"{determiner.capitalize()} {noun} {verb} {prep_phrase}")
        print(sentence)
        i += 1
        counter += 1
    counter = 0
    for j in sentences:
        determiner = get_determiner(quantity_2)
        noun = get_noun(quantity_2)
        verb = get_verb(quantity_2, tense[counter])
        prep_phrase = get_prepositional_phrase(quantity_2)
        sentence = (f"{determiner.capitalize()} {noun} {verb} {prep_phrase}")
        print(sentence)
        j += 1
        counter += 1

def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    word = random.choice(words)
    return word

def get_noun(quantity):
    if quantity == 1:
        words = ["pigeon", "snake", "boy", "car", "cat", "child",
                 "dog", "girl", "man", "bunny", "woman", "person"]
    else:
        words = ["pigeons", "snakes", "boys", "cars", "cats", "children",
                 "dogs", "girls", "men", "bunnies", "women", "people"]
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                 "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think",
                 "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh",
                 "will think", "will run", "will sleep", "will talk",
                 "will walk", "will write"]
    verb = random.choice(verbs)
    return verb


def get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]
    preposition = random.choice(prepositions)
    return preposition

def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    prep_phrase = (f"{preposition} {determiner} {noun}.")
    return prep_phrase

main()