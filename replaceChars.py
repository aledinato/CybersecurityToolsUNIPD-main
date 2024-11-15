def replace_chars(input_string, char_dict):
    result = ""
    for char in input_string:
        result += char_dict.get(char, char)
    return result
