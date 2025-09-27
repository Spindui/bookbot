from stats import *
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    list_of_indvidiual_char_dict = sort_char_counts(get_char_counts(get_book_text(sys.argv[1])))


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print_word_count(sys.argv[1])
    for item in list_of_indvidiual_char_dict:
        ch = item["char"]
        counts = item["num"]
        if ch.isalpha():
            print(f"{ch}: {counts}")
    print("============= END ===============")
