def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_dict(text):
    letter_dict = {}
    letters = [letter for letter in text]
    for letter in letters:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict

def create_dict_report(dictionary):
    for key in dictionary:
        value = key
        print(f"'{key}' was character was found {value} times")

main()