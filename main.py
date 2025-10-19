from stats import get_num_words
from stats import get_character_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def main():
    frankenstein_txt = get_book_text('books/frankenstein.txt')
    word_count = get_num_words(frankenstein_txt)
    get_character_count(frankenstein_txt)
    print(f"Found {word_count} total words")

main()
