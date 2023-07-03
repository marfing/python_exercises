def outer_function():
    x = 10
    def inner_function():
        nonlocal x
        x += 1
        print(f"internal x: {x}")
    print(f"outer x: {x}")
    return inner_function

#closure = outer_function()
#closure()


#li = [10, 20, 30, 20]
#li.remove(20)
#print(li)

def sort(_array):
    print(f"Array to be sorted: {_array}")
    temp = 0
    index = 0
    for key, value in enumerate(_array):
        temp = value
        for i in range(key+1,len(_array)):
            if _array[i] < temp:
                temp = _array[i]
                index = i
        if temp < value:
            _array[index] = value
            _array[key] = temp
            print(f"New array value: {_array}")


sort_array = [10,4,2,56,32,78]

sort(sort_array)

x = "11"
print(int(x,2))