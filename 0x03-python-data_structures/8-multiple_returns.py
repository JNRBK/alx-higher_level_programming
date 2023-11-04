#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        sentence = None, len(sentence)
    s = len(sentence), sentence[0]
    return s
