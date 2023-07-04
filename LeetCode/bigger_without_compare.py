

# return 1 if positive, 0 otherwise
def isPositive(n):
    val = (n >> 33 ) & 1
    return 1 - val 

def my_max(n1,n2):
    diff = n1 - n2
    pos = isPositive(diff)
    return n1*pos + n2*(1-pos)

if __name__ == '__main__':
    print(f'-3 : {bin(-3)}')
    print(f'-3 >> 32: {bin(-3 >> 33)}')
    print(f'3 : {bin(3)}')
    print(f'3 >> 32: {bin(3 >> 33)}')
    print(f'isPositive 3: {isPositive(3)}')
    print(f'isPositive -3: {isPositive(-3)}')
    print(f'Max between 1 and 2: {my_max(1,2)}')
    print(f'Max between 100 and 20: {my_max(100,20)}')
    print(f'Max between -100 and -20: {my_max(-100,-20)}')
