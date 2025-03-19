
def word_count(book_text):
    words = book_text.split()
    word_no = len(words)
    return word_no

def char_count(book_text):
    words = book_text.lower()
    char_dict = {}
    for char in words:
       
        if char.isalpha():

            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] =1
        
    return char_dict

def sort_ch(ch_dict):
    sort_dict = {}
    
    ch_tup = list(ch_dict.items())
    sorted_list = sorted(ch_tup, key=lambda x: x[1], reverse=True)
    sorted_dict = dict(sorted_list)
    return sorted_dict