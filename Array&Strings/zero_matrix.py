class zero_matrix:
    def __init__(self, matrix):
        self.matrix=matrix
        self.n = len(self.matrix[0]) 
        self.x = []
        self.y = []
        print(f"Created a matrix to be zeroed: {self.matrix}")

    def modify_matrix(self):

        for i,row in enumerate(self.matrix):
            for j,value in enumerate(row):
                if value == 0:
                    self.x.append(i)
                    self.y.append(j)
                    print(f"Found zero element, indexes array: {self.x},{self.y}")
        
        for i,row in enumerate(self.matrix):
            for j in range(self.n):
                if j in self.y:
                    print(f"Updating column {j}")
                    row[j] = 0
            if i in self.x:
                print(f"Updating row: {i}")
                self.matrix[i] = [0] * len(row)

    def print_matrix(self):
        print(f"Zeroed matrix: {self.matrix}")


test = [
    [1,3,5,7,9],
    [3,0,3,5,6],
    [5,9,6,0,4]
]
m = zero_matrix(test)
m.modify_matrix()
m.print_matrix()