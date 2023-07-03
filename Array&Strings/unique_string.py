def check_unique (word):
    for i,c in enumerate(word):
        #print(f"i == {i}")
        for ch in word[i+1:]:
            #print(f"Comparing {c} with {ch}")
            if c == ch:
                return "non unico"
    return "unico"

def check_unique_with_hash(word):
    ch_table = {}
    for i,c in enumerate(word):
        if ord(c) in ch_table:
            return "hash - non unico"
        else:
            ch_table[ord(c)] = c
    return "hash - unico"
            
test = "abcdefga"            
print(check_unique(test))            
print(check_unique_with_hash(test))

