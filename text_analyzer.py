#!/usr/bin/python

# text = input()

def text_analyzer(text: str):
    """
    Counts the number of words, uppercase letters, lowercase letters,
     and punctuation characters

    Args:
        text: string of words

    Returns:
        Tuple of the number of words, uppercase letters, lowercase letters
        and punctuation marks
    """
    word_count = 0
    upper_count = 0
    lower_count = 0
    punc_count = 0
    p_marks = [".", ",", "?", "!"]

    for word in range(len(text)):
        if text[word] in p_marks:
            punc_count += 1
        elif text[word].isupper():
            upper_count += 1
        elif text[word].islower():
            lower_count += 1

    return word_count, upper_count, lower_count, punc_count


text = "The default number of decimals is 0, " \
       "meaning that the functIon Will return! the nearest integeR."

result = text_analyzer(text)
print()
print(result)
