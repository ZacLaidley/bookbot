def get_num_words(book_text):
    book_split = book_text.split()
    return len(book_split)

def count_char(book_text):
    book_text = book_text.lower()
    char_dict = {}
    for char in book_text:
        if char in char_dict:
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(letters):
    dict_list = []
    for key in letters:
        letter_dict = {}
        if key.isalpha():
            letter_dict["char"] = key
            letter_dict["num"] = letters[key]
            dict_list.append(letter_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
