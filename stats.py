def count_words(text):
    words = text.split()
    number = 0
    for word in words:
        number += 1
    return number

def count_characters(text):
    low_text = text.lower()
    char_dict = {
        "a": 0
    }
    for character in low_text:
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1
    return char_dict
