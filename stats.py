def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
    
def count_number_of_words(text):
    words = text.split()
    return len(words)

def count_number_of_each_char(text):
    text = text.lower()
    dict = {}
    for i in text:
        if i not in dict.keys():
            dict[i] = 1
            continue
        dict[i] += 1 
    return dict

def structure_and_sort_dict(dict):
    dict_list = []
    for item in dict.items():
        dict_list.append({"char" : item[0], "num": item[1]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def sort_on(items):
    return items["num"]