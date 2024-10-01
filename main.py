def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    dict = {}
    lower_string = text.lower()
    for char in lower_string:
        if char.isalpha():
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
    return dict

def sort_on(dict):
    return dict["num"]

def dict_to_list(dict):
    list = []
    for key in dict:
        list.append({"char": key, "num": dict[key]})
    list.sort(reverse=True, key=sort_on)
    return list

def main():
    book_path = "github.com/TesrSK/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    char = count_char(text)
    list = dict_to_list(char)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    for dict in list:
        print(f"The {dict['char']} character was found {dict['num']} times")
    print("--- End report ---")

main()