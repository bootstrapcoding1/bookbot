def get_num_words(string):
    new_string = string.split()
    return len(new_string)

def get_character_count(string):
    new_string = string.lower()
    character_set = set()
    character_dict = dict([])
    for char in new_string:
        if char not in character_set:
            character_set.add(char)
        if not (char in character_dict):
            character_dict[char] = 1
        else:
            character_dict[char] += 1
    return character_dict

def sort_on(items):
    return items["num"]

def  single_char_dictionary(char, number):
    dictionary = {
        "char": char,
        "num": number
    }
    return dictionary

def dictionary_to_list(dictionary):
    list_of_chars = []
    for item in dictionary:
        list_of_chars.append(single_char_dictionary(item, dictionary[item]))
    return list_of_chars

def print_dictionary(list_of_chars):
    for dict in list_of_chars:
        if dict["char"].isalpha():
            char = dict["char"]
            num = dict["num"]
            print(f"{char}: {num}")