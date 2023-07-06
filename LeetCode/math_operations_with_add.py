def my_multiply(x : int,y : int):
    if x == 0 or y == 0:
        return 0
    if abs(x) != x and abs(y) == y:
        values = (y,x)
    elif abs(y) != y and abs(x) == x:
        values = (x,y)
    else:
        values = (abs(x),abs(y)) if abs(x) < abs(y) else (abs(y),abs(x))
    sum = values[1]
    for i in range(values[0]-1):
        sum += values[1]
    return sum

def my_int_division(x: int, y : int):
    if y > x:
        return 0
    count = 0
    divider = y
    while divider <= x:
        count += 1
        divider += y
    return count

if __name__ == '__main__':
    print(f'3x2 = {my_multiply(3,2)}')
    print(f'-3x2 = {my_multiply(-3,2)}')
    print(f'3x-2 = {my_multiply(3,-2)}')
    print(f'-3x-2 = {my_multiply(-3,-2)}')

    print(f'4/2 = {my_int_division(4,2)}')
    print(f'2/4 = {my_int_division(2,4)}')