#Takes a relative or full path of text file and reads it.
def get_book_text(path):
    with open(path) as f:
        return f.read()
#Takes input from get_book_text. Counts the number of words in the text.
def count_words(text):
    words = text.split()
    return len(words)
#Takes input from get_book_text. Counts the number of characters that are repeating, if it doesn't exist it adds the character and sets it to 1.
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
#Sort numbers for dict_to_list function or .sort(key=)
def sort_on(dict):
    return dict["num"]
#Takes a dictionary and turn it into a list with dictionaries, puts characters into "char" and the number of the character in "num" then it sorts it in reverse (highest number to lowest)
def dict_to_list(dict):
    list = []
    for key in dict:
        list.append({"char": key, "num": dict[key]})
    list.sort(reverse=True, key=sort_on)
    return list
#Main function that runs everything
def main():
    #Variables
    book_path = "github.com/TesrSK/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    char = count_char(text)
    list = dict_to_list(char)
    #Report
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    for dict in list:
        print(f"The {dict['char']} character was found {dict['num']} times")
    print("--- End report ---")

main()