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

def sort_on(char):
    return char["num"]

def sort_characters(char_dict):
    sorted_list = []
    for ch in char_dict:
        sorted_list.append({"char": ch, "num": char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

# Alternative Lösung Sortierung
#def sort_characters(char_dict):
#    return dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
