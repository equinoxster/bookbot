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

def pretty_print(char_dict):
    ordered = []
    for key in char_dict.keys():
        ordered.append({"char": key, "num": char_dict[key]})

    ordered.sort(reverse=True, key=sort_on)
    return ordered


def sort_on(dict):
    return dict["num"]
