# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).


def string_compression(string1):
    
    temp_string = ''
    temp_char = ''
    temp_counter = 0
    
    for i,c in enumerate(string1):
        print(f"Checking character: {c} - temp_char: {temp_char} - temp_counter: {temp_counter}")
        if i == 0:
            temp_char = c
            temp_counter = 1
            continue
        if temp_char == c:
            temp_counter += 1
        else:
            temp_string += temp_char + str(temp_counter)
            temp_char = c
            temp_counter = 1

    temp_string += temp_char + str(temp_counter)    
    if len(string1) == len(temp_string):
        return string1
    else:
        return temp_string
