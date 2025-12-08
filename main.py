from stats import word_count
from stats import character_count
from stats import dict_sort

def get_book_contents(filepath):
    book_text = None
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    file_path = "books/frankenstein.txt"
    dict_lst = dict_sort(character_count(get_book_contents(file_path)))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(get_book_contents(file_path))} total words")
    print("--------- Character Count -------")
    for dict in dict_lst:
        if dict["char"].isalpha() == True:
            print(f"{dict["char"]}: {dict["num"]}")
        else:
            continue
    print("============= END ===============")



main()