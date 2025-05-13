#!/usr/bin/python3

def multiple_returns(sentence):
    # Return the length of the sentence and its first character
    if sentence == "":
        # If the sentence is empty, return 0 and None
        return (0, None)
    # If the sentence is not empty, return its length and first character
    else:
        # Return the length of the sentence and its first character
        return (len(sentence), sentence[0])
