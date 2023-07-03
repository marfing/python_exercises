

def is_palindrome_permutation(string1):
    count_odd = 0
    table = {}
    string1 = string1.lower()
    for c in string1:
        if c == " ":
            continue
        ascii = ord(c)
        if ascii in table:
            value = table[ascii] + 1 
            table[ascii] = value
            if value % 2 != 0:
                count_odd = count_odd + 1
            else:
                count_odd = count_odd - 1
        else:
            table[ascii] = 1
            count_odd += 1
        print(f"Char: {c} Table: {table} - counter: {count_odd}")

    if count_odd == 1:
        return True
    else:
        return False

test = "Tact Coa"
print(f"Check the string {test} with result {is_palindrome_permutation(test)}")