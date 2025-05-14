from stats import get_num_words
from stats import count_char
from stats import sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main(book_path):
    book_text = get_book_text(f"{book_path}")
    num_words = get_num_words(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    char_count = count_char(book_text)
    char_sort = sort_dict(char_count)
    print("--------- Character Count -------")
    for item in char_sort:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])
