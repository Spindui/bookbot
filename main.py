from stats import *

if __name__ == "__main__":
    print_word_count('books/frankenstein.txt')
    list_of_inv_nums = get_char_counts(get_book_text('books/frankenstein.txt'))
    print(list_of_inv_nums)