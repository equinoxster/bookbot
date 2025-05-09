def get_num_words(path_to_file) :
    with open(path_to_file) as f:
        # do something with file here
        file_contents = f.read()
        word_count = len(file_contents.split())
        return word_count