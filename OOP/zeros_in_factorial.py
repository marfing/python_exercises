class factorial_calc():
      

    def find_last_zeros(self,n):
        k = 1
        count = 0
        while (j := 5**k) < n:
            count += n//j
            k += 1
        return count

if __name__ == '__main__':
    fact = factorial_calc()

    n = 1000
    print(f'Found {fact.find_last_zeros(n)} zeros')