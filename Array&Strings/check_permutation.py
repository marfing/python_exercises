

def check_is_permutation(string1, string2):
    if len(string1) != len(string2):
        return False
    
    table = {}
    for c in string1:
        if ord(c) in table:
            table[ord(c)] =  table[ord(c)] + 1
        else:
            table[ord(c)] = 1
    
    for c in string2:
        if ord(c) in table:
            if table[ord(c)] > 0:
                table[ord(c)] =  table[ord(c)] - 1
            else:
                return False
        else:
            return False
    
    return True


test1 = "pippo"
test2 = "oppep"
print(f"Checking {test1} with {test2} - result: {check_is_permutation(test1, test2)}")