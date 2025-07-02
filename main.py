import sys
from stats import (
    count_words,
    count_characters,
    sort_characters,
)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    #Get stuff
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_dir = None
    for argument in sys.argv:
        if "books/" in argument:
            book_dir = sys.argv[1]
    if book_dir == None:
        raise Exception("directory not found")
    text = get_book_text(book_dir)
    number_of_words = count_words(text)
    dict_of_chars = count_characters(text)
    ordered_dict = sort_characters(dict_of_chars)
   
    #Print stuff
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_dir}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for character in ordered_dict:
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")

main()
