def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def count_words(text):
    words = text.split()
    number = 0
    for word in words:
        number += 1
    return number

def main():
    text = get_book_text("./books/frankenstein.txt")
    number_of_words = count_words(text)
    print(f"{number_of_words} words found in the document")

main()