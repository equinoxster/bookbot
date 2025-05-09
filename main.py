def get_book_text(path_to_file) :
    with open(path_to_file) as f:
        # do something with file here
        file_contents = f.read()
        return file_contents

def main():
     content = get_book_text("./books/frankenstein.txt")
     word_count = len(content.split())
     print(f"{word_count} words found in the document")

main()
