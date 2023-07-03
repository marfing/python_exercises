#One Away: There are three types of edits that can be performed on strings: insert a character,
#remove a character, or replace a character. Given two strings, write a function to check if they are
#one edit (or zero edits) away.
#EXAMPLE
#pale, ple -> true
#pales, pale -> true
#pale, bale -> true
#pale, bake -> false

def one_away(str1, str2):
    insert_counter = 0
    remove_counter = 0
    replace_counter = 0
    len1 = len(str1)
    len2 = len(str2)
    for i,c in enumerate(str1):
        #print(f"Index: {i} - value: {c}")
        if i+insert_counter-remove_counter >= len2:
            remove_counter += 1
            #print(f"str1 bigger thatn str2 - remove_counter: {remove_counter}")
            continue
        if c == str2[i+insert_counter-remove_counter]:
            #print(f"c1: {c} == c2: {str2[i+insert_counter-remove_counter]}")
            continue
        #insert
        elif len(str2)-insert_counter > len1:
            insert_counter += 1
            #print(f"insert_counter: {insert_counter}")
        #remove
        elif len(str2)-remove_counter < len1:
            remove_counter += 1
            #print(f"remove_counter: {remove_counter}")
        #replace
        else:
            replace_counter +=1
            #print(f"Replace_counter: {replace_counter}")
             
    if insert_counter + remove_counter + replace_counter > 1: 
        return False
    return True


 
