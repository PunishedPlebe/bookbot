def word_count(book_text):
    word_lst = book_text.split()
    word_count = 0
    for word in word_lst:
        word_count += 1
    return word_count

def character_count(book_text):
    found_char = {} #create a dictonary to store character:count(int) pairs
    for character in book_text: #for each character in the passed string
        lower_char = character.lower()
        if lower_char not in found_char: # if character is not in the dictonary
            #print(f"{lower_char} is not present. adding to dictionary...") #print the character to verify what we're working with and how far we got
            found_char[lower_char] = 1 #set the default value of the key(character) to a val of 0
            #print(found_char) # print the dictonary to ensure results
        else: # if the character is present in the dictonary
            found_char[lower_char] = found_char[lower_char] + 1 #set the value of dictonary at key[character] : to it's current value + 1
    return found_char

def sort_on(items): # function takes dictionary and returns the value stored in num key
    return items["num"]

def dict_sort(dict): #function that sorts entries in a dictionary
    dict_lst = [] #create a holder list for the dictionaries
    holder_dict = {} #create a holder dictonary to restucture the character_count output dictionary
    
    for entry in dict: # for each entry in the character_count output dictionary
        holder_dict = {"char" : entry , "num" : dict[entry]} #create a dictionary with 2 keys "char" : character value stored in dict and "num" : int value stored in dict for that character
        dict_lst.append(holder_dict) #append the holder dictionary to the dict_lst to create a list of dictionary entires
        holder_dict = {} #reset the holder dictionary to empty
    dict_lst.sort(reverse=True, key=sort_on) #sort the dictionary list in decending order by the value stored in "num" key
    return(dict_lst) #return the list of sorted dictionary entries
