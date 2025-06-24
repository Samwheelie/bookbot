def word_count(text):
    text_array = text.split()
    return len(text_array)

def number_repeated_chars(text):
    lower = text.lower()
    result = {}
    for letter in lower:
        if(letter == ' '):
            pass
        elif(letter in result):
            result[letter] += 1
        else:
            result[letter] = 1

    return result

def sort_on(list):
    return list["num"]

def sort_char_dict(char_dict):
    list = []
    for entry in char_dict:
        list.append({"char": entry, "num": char_dict[entry]})
    
    list.sort(reverse=True, key=sort_on)

    return list

