from stats import get_num_words
from stats import get_character_count
from stats import dictionary_to_list
from stats import sort_on
from stats import print_dictionary
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def validate_sys_argv(argv_list):
    if not (len(argv_list) == 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():
    validate_sys_argv(sys.argv)

    path_to_book = sys.argv[1]
    book = get_book_text(path_to_book)

    word_count = get_num_words(book)
    print(f"Found {word_count} total words")

    dictionary = get_character_count(book)
    print(dictionary)

    list = dictionary_to_list(dictionary)
    list.sort(reverse=True, key=sort_on)
    print_dictionary(list)

main()
