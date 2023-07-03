
def multRecursive(n,m,temp_n=0):
    if m > 1:
        temp_n = temp_n + (n << 1)
        m = m -2
        if m > 0:
            return multRecursive(n,m,temp_n)
    return temp_n + n


if __name__ == '__main__':
    n = 9
    m = 9
    print(multRecursive(n,m))