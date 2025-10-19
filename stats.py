def get_num_words(string):
    new_string = string.split()
    return len(new_string)

def get_character_count(string):
    new_string = string.lower()
    character_set = set()
    for char in new_string:
        if char not in character_set:
            character_set.add(char)

    return new_string