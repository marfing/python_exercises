
# You are give two 32-bit numbers, N and M, and two bit positions, i and j. 
# Write a method to insert M into N such that M starts at bit j and ends at bit i.
# Yuo can assume that the bits j through i have enough space to fit all of M.
# That is, if M = 10011, you can assume that there are at least 5 bits between j and i.
# You would not, for example, have j = 3 and i = 2, because M could not fully fit between bit 3 and 2

# Example:
# Input: N = 10000000000, M = 10011, i = 2, J = 6
# Output: N = 10001001100


def clear(N,i):
    result = N & (~(1 << i))
    return result

def clearRange(N,from_j,to_i):
    result = N
    for i in range(to_i, from_j):
        result = clear(result,i)
    return result

def insert(N,M,j,i):
    print(f'Inserting {M:b} in {N:b} between {i} and {j}')
    N = clearRange(N,j,i)
    print(f'After range clearing {N:b}')
    M = M << i
    print(f'M after left swift {M:b}')
    result = N | M
    print(f'Final result: {result:b}')
    return

#convert and int in a binary string
def binaryToString(n):
    stop = False
    s = ''
    while not stop:
        s += str(n % 2)
        n = n // 2
        if n == 0:
            stop = True
    return s[::-1]


#count the binary size of an int
def binaryToStringLenght(n):
    return len(binaryToString(n))

#conta il numero massimo di 1 successivi permettendo la conversione di un solo 0 in 1
#uso una maschera con un solo 1 che attraversa tutto il numero analizzando i singoli bit ed incrementando opportunamente i contatori
def flipBitToWin(N):
    i = 0
    count = 0
    count2 = 0
    flipped = False
    best = 0
    for i in range(binaryToStringLenght(N)):
        mask = 1 << i
        result = N & mask
        if result > 0:
            count += 1
            count2 += 1
            if count > best:
                best = count #salva il precedente numero di 1 consecutivi + 0 modificato
        elif not flipped: #trova primo zero
            flipped = True
            count += 1
            count2 = 0
        else: #trova un altro zero
            if count2 == 0: #zeri consecutivi
                count = 0
                flipped = False
            else: #zero dopo sequenza di 1
                count = count2 + 1 #riparte dalla sequenza di 1 successivi al primo zero trovato + lo zero attuale modificato
                count2 = 0
    return best

#  Given a positive integer, print the next smallest and the next largest number that
# have the same number of 1 bits in their binary representation
def nextBiggerNumberBF(N):
    if N < 0: 
        print(f'Next number woirks only if input number is positive. You have entered {N}')            
        return
    ones_n = countOnes(N)
    found = False
    while not found:
        N = N+1
        if ones_n == countOnes(N):
            found = True
    return N

def nextBiggerNumber(N):
    if N < 0: 
        print(f'Next number woirks only if input number is positive. You have entered {N}')            
        return
    less_imp_index = None
    binary = binaryToString(N)
    binary_len = binaryToStringLenght(N)
    for i in range(binary_len):
        mask = 1 << i
        result = N & mask
        if result > 0 and less_imp_index == None: #trovato un 1 salvo il suo indice
            less_imp_index = i
        elif result == 0 and less_imp_index != None: #trovato uno zero libero dove spostare l'1 meno rilevante
            binary = changeCharInString(binary,'0',(binary_len-1)-less_imp_index)
            binary = changeCharInString(binary,'1',(binary_len-1)-i)
            return int(f'0b{binary}',2)
    #nel caso in cui ci sia un solo 1 e sia il più rilevante (es. 1000)
    if less_imp_index == binary_len-1:
        binary = changeCharInString(binary,'0',0)
        return int(f'0b1{binary}',2)
    else: #tutti 1
        print(f'cannot find bigger value with same 1s number')
        return int(f'0b{binary}',2)
    

def changeCharInString(s,char,index):
    return s[:index] + char + s[index+1:]

def countOnes(N):
    bin = binaryToString(N)
    return bin.count('1')

def swapInPlace(a, b):
    # shift a << n (capire di quante posizioni pari ai bit di rappresentazione di b)
    # sommare b che andrà ad occupare i primi bit da destra
    # b = a >> n
    # 
    #print(f'b: {bin(b)}')
    #print(f'a: {bin(a)}')
    a = a << 32
    #print(f'a << 32: {bin(a)}')
    a = a + b
    #print(f'a + b: {bin(a)}')
    b = a >> 32
    #print(f'b = a >> 32: {bin(b)}')
    mask = (1 << 32)-1
    #print(f'mask : {bin(mask)}')
    a = a & mask
    #print(f'a: {bin(a)}')
    return a,b
    #a = a  
    #pass

if __name__ == "__main__":
    M = '0b10011'
    N = '0b1111111111110011101111'
    i = 2
    j = 6
    n_test = 8

    #print(f"{number:b}"")
    #insert(int(N,2),int(M,2),j,i)
    #print(f'Value {n_test} to binary: {binaryToString(n_test)}')
    #print(f"Max number of consecutive 1s converting just a 0 to 1: {flipBitToWin(int(N,2))}")
    #print(f'Next bigger integer with same number of 1s for {n_test} is {nextBiggerNumberBF(n_test)}')
    #print(f'Next bigger integer with same number of 1s for {n_test} is {nextBiggerNumber(n_test)}')

    print(f'i: {i}, j:{j}')
    i,j = swapInPlace(i,j)
    print(f'After swap - i: {i}, j:{j}')