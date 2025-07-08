import sys
from stats import word_count,character_count, sorted_character_list_of_dictionaries

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

rel_file_path = sys.argv[1]  
    

#given a file path saves the text file as string
def get_book_text(file_path):
    with open(file_path) as f:
        book_contents = f.read()
    return book_contents

#variables set for printing purposes that refer to functions created to process the data in the stats.py file

book = get_book_text(rel_file_path)
book_char_count = character_count(book)
num_words = word_count(book)
char_dict_list = sorted_character_list_of_dictionaries(book_char_count)
#Everything below here is printing the report
print("============ BOOKBOT ============")
print(f"Analyzing book found at {rel_file_path}")
print("----------- Word Count ----------")
print(f"Found {num_words} total words ")
print("--------- Character Count -------")
for item in char_dict_list:
    print(f"{item["char"]}: {item["num"]}")




