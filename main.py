from stats import *

if __name__ == "__main__":
    list_of_indvidiual_char_dict = sort_char_counts(get_char_counts(get_book_text('books/frankenstein.txt')))


    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print_word_count("books/frankenstein.txt")
    for item in list_of_indvidiual_char_dict:
        ch = item["char"]
        counts = item["num"]
        if ch.isalpha():
            print(f"{ch}: {counts}")
    print("============= END ===============")
