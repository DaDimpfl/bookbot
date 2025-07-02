def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    from stats import count_words, count_characters
    
    text = get_book_text("./books/frankenstein.txt")
    number_of_words = count_words(text)
    dict_of_chars = count_characters(text)

    print(f"{number_of_words} words found in the document")
    for character in dict_of_chars:
        print(f"'{character}': {dict_of_chars[character]}")

main()