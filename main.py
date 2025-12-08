from stats import word_count
from stats import character_count
from stats import dict_sort

def get_book_contents(filepath):
    book_text = None
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    print("")
    print("Calculating the word count...")
    print(f"Found {word_count(get_book_contents("books/frankenstein.txt"))} total words")
    print("")
    print("Generating list of dictionaries holding character and count values...")
    print(f"{dict_sort(character_count(get_book_contents("books/frankenstein.txt")))}")

main()