def get_num_words(text) :
    word_count = len(text.split())
    return word_count
    
def get_char_count(text):
    lower_case_text = text.lower()
    chars = {}
    for c in lower_case_text:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars