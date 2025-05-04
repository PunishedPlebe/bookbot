from stats import *
import sys

if len(sys.argv) != 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    title = sys.argv[1]
    print(sys.argv[1])



def main():
    #print(get_book_text("frankenstein"))
    #print(f"{word_count(get_book_text("frankenstein"))} words found in the document")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{title}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(get_book_text(title))} total words")
    #print(f"Found {character_count(get_book_text("frankenstein"))} total words" )
    print("--------- Character Count -------")
    for pair in report(character_count(get_book_text(title))):
        for val in pair:
            print(f"{val}: {pair.get(val)}")
    #print(f"{report(character_count(get_book_text("frankenstein")))}")
    print("============= END ===============")


main()
