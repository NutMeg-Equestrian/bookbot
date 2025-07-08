#takes a single long string and counts how many words are in it
def word_count(book_text):
    all_words = book_text.split()
    count = 0
    for i in all_words:
        count += 1
    return count

#takes a single long string and counts how many characters, spaces and punctuation included, are in it
def character_count(book_text):
    char_dict = {}
    book_text_lower = book_text.lower()

    for char in book_text_lower:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

#a lemma function that will help us get ahold of a second mini-dictionary entry and sort by the value there
def sort_on(items):
    return items["num"]

#takes the output of character_count and creates a list of mini dictionaries containing a lable and the specific thing associated with the label for each entry in the orginal dictionary
def sorted_character_list_of_dictionaries(d):
    list_of_dictionaries = []
    new_dictionary = {}
    for key in d:
        if key.isalpha(): #they didn't want spaces and punctuation counted so this helps us skip non-alpha entries
            new_dictionary = {"char":key, "num":d[key]}
            list_of_dictionaries.append(new_dictionary)
    
    list_of_dictionaries.sort(reverse=True,key=sort_on)
    
    return list_of_dictionaries


    