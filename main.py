def get_book_contents(filepath):
    book_text = None
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    print(get_book_contents("books/frankenstein.txt"))

main()