def get_word_count(file_contents: str):
    words = file_contents.split()
    num_words = len(words)
    return num_words

def get_book_text(filepath: str):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_word_count(filepath: str):
    file_contents = get_book_text(filepath)
    num_words = get_word_count(file_contents)       
    print(f"Found {num_words} total words")

def get_char_counts(file_contents: str):
    file_contents = file_contents.lower()
    num_of_char_dict = {}
    for char in file_contents:
        if char in num_of_char_dict:
                num_of_char_dict[char] += 1
        else:
             num_of_char_dict[char] = 1
    return num_of_char_dict

def sort_char_counts(char_dictionary: dict):
    items = create_individual_dict_for_list(char_dictionary)
    items.sort(reverse= True, key=sort_on)
    return items

def sort_on(items):
    return items["num"]

def create_individual_dict_for_list(char_dictionary: dict)-> list:
    list_of_dicts = []
    for k, v in char_dictionary.items():
        list_of_dicts.append({"char": k, "num": v})
    return list_of_dicts
     