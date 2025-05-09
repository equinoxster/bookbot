def get_book_text(path_to_file) :
    with open(path_to_file) as f:
        # do something with file here
        file_contents = f.read()
        return file_contents

def main():
     content = get_book_text("./books/frankenstein.txt")
     print(content)

main()
