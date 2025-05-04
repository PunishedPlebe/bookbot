def get_book_text(title):
    with open(title) as f:
        file_contents = f.read()
        return file_contents

def word_count(book):
    word_count = 0
    for words in book.split():
        word_count += 1
    return word_count

def character_count(book):
    characters_count={}
    for char in book:
        char = char.lower()
        if char in characters_count:
            characters_count[char] += 1
        else:
            characters_count[char] = 1
    return characters_count

def report(dict):
    temp_list = []
    sorted_list = []
    for entry in dict:
        if entry.isalpha():
            temp_list.append((dict[entry], entry))
    temp_list.sort(reverse=True)
    for pair in temp_list:
        temp_dict = {pair[1]:pair[0]}
        sorted_list.append(temp_dict)
    return sorted_list
