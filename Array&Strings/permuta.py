
def insert_new_char(permutation_list, new_char):
    out_come = []
    if len(permutation_list) == 0:
        return [new_char]
    for word in permutation_list:
        for i in range(len(word)+1):
            print(f'index {i} in word {word} range {len(word)} new char {new_char}')
            l_string = [c for c in word]
            l_string.insert(i, new_char)
            out_come.append("".join(l_string))
    return out_come

def permuta(word):
    permutations = []
    for c in word:
        permutations = insert_new_char(permutations, c)
        print(permutations)
    return permutations

print(permuta('tes'))