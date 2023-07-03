class board:
    def __init__(self, size = 3):
        self.size = size
        self.b = [ ['' for i in range(size)] for j in range(size)]
        # self.b = [[ box() for i in range(size)] for j in range(size)]
        # for i in range(size):
        #     for j in range(size):
        #         if i > 0:
        #             self.b[i][j].setUp(self.b[i-1][j])
        #         if i < size-1:
        #             self.b[i][j].setDown(self.b[i+1][j])
        #             if i == j:
        #                 self.b[i][j].setRightDiag(self.b[i+1][j+1])
        #             if (i + j) == size-1:
        #                 self.b[i][j].setLefDiag(self.b[i+1][j-1])
        #         if j > 0:
        #             self.b[i][j].setLeft(self.b[i][j-1])
        #         if j < size-1:
        #             self.b[i][j].setRight(self.b[i][j+1])
        
    def __repr__(self) -> str:
        return f'{self.b}'
    
    def setValue(self, x: int,y: int,value: str):
        #self.b[x][y].setValue(value)
        self.b[x][y] = value

    def checkWin(self, last_x, last_y, value):
        return self.checkRowWin(value, last_x) or self.checkColumnWin(value, last_y) or self.checkDiagWin(value, last_x, last_y)        

    def setValueAndCheckWin(self, x: int,y: int,value: str) -> bool:
        self.setValue(x,y,value)
        return self.checkWin(x,y, value)
    
    def checkRowWin(self, value,row):
        for j in range(self.size):
            if self.b[row][j] != value:
                return False
        return True
    
    def checkColumnWin(self, value, col):
        for i in range(self.size):
            if self.b[i][col] != value:
                return False
        return True

    def checkDiagWin(self, value, row, col):
        if row == col:
            for i in range(self.size):
                if self.b[i][i] != value:
                    return False
            return True
        elif row + col == self.size-1:
            for i in range(self.size):
                if self.b[i][self.size-1-i] != value:
                    return False
            return True
        else:
            return False
    
# class box:
#     def __init__(self, l = None, r = None, u= None, d = None, ld = None, rd = None):
#         self.l = l
#         self.r = r
#         self.u = u
#         self.d = d
#         self.ld = ld
#         self.rd = rd
#         self.value = 'Empty'
    
#     def setValue(self, value):
#         self.value = value
    
#     def setLeft(self, box):
#         self.l = box
    
#     def setRight(self, box):
#         self.r = box

#     def setUp(self, box):
#         self.u = box

#     def setDown(self, box):
#         self.d = box

#     def setLefDiag(self, box):
#         self.ld = box

#     def setRightDiag(self, box):
#         self.rd = box        

#     def __repr__(self) -> str:
#         return self.value
    
#     def hasLeftMatch():
#         if self.


if __name__ == '__main__':
    b = board(4)
    print(b)
    b.setValue(0,0,'X')
    if b.setValueAndCheckWin(1,1,'X'):
        print(f'We have a winner!! : {b}')
    else:
        print(b)
    if b.setValueAndCheckWin(2,2,'X'):
        print(f'We have a winner!! : {b}')
    else:
        print(b)
    
    