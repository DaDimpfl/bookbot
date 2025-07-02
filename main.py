from stats import (
    count_words,
    count_characters,
    sort_characters,
)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    #Define stuff
    book_dir = "books/frankenstein.txt"
    
    #Get stuff
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
