from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest

quantity_1 = 1
quantity_2 = 2
tense = ["past", "present", "future"]

def test_get_determiner():
    single_determiners = ["a", "one", "the"]
    for _ in range(4):
        word = get_determiner(1)
        assert word in single_determiners
    plural_determiners = ["some", "many", "the"]
    for _ in range(4):
        word = get_determiner(2)
        assert word in plural_determiners

def test_get_noun():
    single_nouns = ["pigeon", "snake", "boy", "car", "cat", "child",
                    "dog", "girl", "man", "bunny", "woman", "person"]
    for _ in range(4):
        noun = get_noun(1)
    assert noun in single_nouns
    plural_nouns = ["pigeons", "snakes", "boys", "cars", "cats", "children",
                    "dogs", "girls", "men", "bunnies", "women", "people"]
    for _ in range(4):
        noun = get_noun(2)
    assert noun in plural_nouns

def test_get_verb():
    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
                  "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(4):
        verb = get_verb(1, "past")
    assert verb in past_verbs
    single_present_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                            "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(4):
        verb = get_verb(1, "present")
    assert verb in single_present_verbs
    plural_present_verbs = ["drink", "eat", "grow", "laugh", "think",
                            "run", "sleep", "talk", "walk", "write"]
    for _ in range(4):
        verb = get_verb(2, "present")
    assert verb in plural_present_verbs
    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
                    "will think", "will run", "will sleep", "will talk",
                    "will walk", "will write"]
    for _ in range(4):
        verb = get_verb(1, "future")
    assert verb in future_verbs

def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]
    for _ in range(0, len(prepositions)):
        preposition = get_preposition()
    assert preposition in prepositions

def test_get_prepositional_phrase():
    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]
    for _ in range(0, len(prepositions)):
        preposition = get_preposition()
    assert preposition in prepositions
    determiners = ["a", "one", "some", "many", "the"]
    for _ in range(0, len(determiners)):
        determiner = get_determiner(1)
    assert determiner in determiners
    nouns = ["pigeon", "snake", "boy", "car", "cat", "child",
             "dog", "girl", "man", "bunny", "woman", "person", "pigeons", "snakes", "boys", "cars", "cats", "children",
             "dogs", "girls", "men", "bunnies", "women", "people"]
    for _ in range(0, len(nouns)):
        noun = get_noun(1)
    assert noun in nouns

pytest.main(["-v", "--tb=line", "-rN", __file__])