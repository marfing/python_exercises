class Sorter:
    def __init__(self, items: list):
        self.items = items

    # Bubble Sort I Runtime: 0( n2) average and worst case. Memory: 0( 1)
    # In bubble sort, we start at the beginning of the array and swap the first two elements if the first is greater
    # than the second.Then, we go to the next pair, and so on, continuously making sweeps of the array until it is
    # sorted. In doing so, the smaller items slowly"bubble"up to the beginning of the list
    
    def bubbleSort(self):
        exit = False
        while not exit:
            exit = True
            for index,item in enumerate(self.items):
                if index < len(self.items)-1:
                    if self.items[index] > self.items[index+1]:
                        self.items[index] = self.items[index+1]
                        self.items[index+1] = item
                        exit = False
        print(f'Bubble sort: {self.items}')


    # Selection Sort I Runtime: 0( n2 ) average and worst case. Memory: 0( 1) .
    # Selection sort is the child's algorithm: simple, but inefficient. Find the smallest element using a linear scan
    # and move it to the front (swapping it with the front element). Then, find the second smallest and move it,
    # again doing a linear scan. Continue doing this until all the elements are in place.

    def selectionSort(self):
        exit = False
        while not exit:
            min = self.items[0]
            exit = True
            for index, value in enumerate(self.items):
                if value < min:
                    self.items[index] = min
                    self.items[0] = value
                    exit = False
        print(f'Selection Sort: {self.items}')


    # ricordarsi sempre che per ogni chiamata ricorsiva arr è passato per riferimento, quindi una volta
    # riordinato dal basso, risale negli step precedenti che potranno usare arr come L o R a seconda di dove ci si trova
    def mergeSort(self, arr):
        print(f'mergeSort: {arr}')
        if len(arr) > 1:
            #find mid of the array
            middle = len(arr)//2
            # Sorting the first half
            L = arr[:middle]
            self.mergeSort(L)
            # Sorting the second half
            R = arr[middle:]
            self.mergeSort(R)

            i = j = k = 0

            #Copy data to temp arrays L and R
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            #Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        print(f'merge sort bottom: {arr}')


    # In quick sort we pick a random element (nel nostro caso sempre l'ultimo valore a dx) and partition the array, such that all numbers that are less than the
    # partitioning element come before all elements that are greater than it. The partitioning can be performed
    # efficiently through a series of swaps

    def quickSort(self, arr):
        print(f'Quick Sorting: {arr}')
        range = len(arr)-1
        pivot = arr[range]
        R = []
        i = j = 0
        
        while i < range:
            if arr[i] <= pivot:
                arr[j] = arr[i]
                j += 1
            else:
                R.append(arr[i])
            i += 1

        arr[j] = pivot
    
        if j > 1:
            self.quickSort(arr[:j])
            if len(R) > 0:
                arr[j+1:] = R
                self.quickSort(arr[j:])
        
        print(f'Sorted array: {arr}')

    # Radix Sort is a linear sorting algorithm that sorts elements by processing them digit by digit.
    # It is an efficient sorting algorithm for integers or strings with fixed-size keys. 
    def radixSort(self):
        pass


if __name__ == '__main__':
    items = [10,80,30,90,40,50,70]
    sorter = Sorter(items)
    # sorter.bubbleSort()
    # sorter.selectionSort()
    #sorter.mergeSort(items)
    sorter.quickSort(items)