def get_num_of_words(file_contents: str):
    words = file_contents.split()
    num_words = len(words)
    return num_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_contents = get_book_text('books/frankenstein.txt')
    num_words = get_num_of_words(file_contents)       
    print(f"Found {num_words} total words")