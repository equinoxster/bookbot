from stats import get_num_words, get_char_count

def main():
     path = "./books/frankenstein.txt"
     text = get_book_text(path)
     words = get_num_words(text)
     
     print(f"{words} words found in the document")
     char_dict = get_char_count(text)
     print(char_dict)


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # do something with file here
        file_contents = f.read()
        return file_contents
    
main()
