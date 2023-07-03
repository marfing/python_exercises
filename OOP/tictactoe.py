class board:
    def __init__(self, size = 3):
        self.size = size
        self.b = [ ['' for i in range(size)] for j in range(size)]
        
    def __repr__(self) -> str:
        return f'{self.b}'
    
    def setValue(self, x: int,y: int,value: str):
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
    
    