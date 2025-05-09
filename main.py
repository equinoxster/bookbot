from stats import get_num_words, get_char_count, pretty_print

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    words = get_num_words(text)
     
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    char_dict = get_char_count(text)

    ordered = pretty_print(char_dict)
    # print(ordered)
    for i in range(0, len(ordered)):
        print(f"{ordered[i]['char']}: {ordered[i]['num']}")
    print("============= END ===============")


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # do something with file here
        file_contents = f.read()
        return file_contents
    
main()
