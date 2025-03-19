from stats import word_count, char_count, sort_ch
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def format(path,word_no,sort_char):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_no} total words.")
    print("--------- Character Count -------")
    for i in sort_char:
        print(f"{i}: {sort_char[i]}")
    print("============= END ===============")
    return    


def main():
    contents = get_book_text(sys.argv[1])
    word_no = word_count(contents)
    letters = char_count(contents)
    #print(letters)
    sort_char = sort_ch(letters)
    #print(sort_char)
    #print(len(sys.argv))
    format(sys.argv[1],word_no,sort_char)


if len(sys.argv) == 2:
    main()
else:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
