from stats import get_num_words
from stats import get_character_count
from stats import dictionary_to_list
from stats import sort_on
from stats import print_dictionary

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def main():
    frankenstein_txt = get_book_text('books/frankenstein.txt')
    word_count = get_num_words(frankenstein_txt)
    print(f"Found {word_count} total words")
    dictionary = get_character_count(frankenstein_txt)
    print(dictionary)
    list = dictionary_to_list(dictionary)
    list.sort(reverse=True, key=sort_on)
    print_dictionary(list)

main()
