class converter:
    def __init__(self):
        self.map = {
            0:'zero',
            1:'one',
            2:'two',
            3:'three',
            4:'four',
            5:'five',
            6:'six',
            7:'seven',
            8:'eight',
            9:'nine',
            10:'ten',
            11:'eleven',
            12:'twelve',
            13:'thirteen',
            14:'fourteen',
            15:'fifteen',
            16:'sixteen',
            17:'seventeen',
            18:'eighteen',
            19:'nineteen',
            20:'twenty',
            30:'thirty',
            40:'fourty',
            50:'fifty',
            60:'sixty',
            70:'seventy',
            80:'eighty',
            90:'ninety',
        }
        self.unit = {
            0 : '',
            3 : 'thousand',
            6 : 'milion',
            9 : 'bilion',
            12: 'trilion'
        }

    def toEnglish(self, n):
        #n = str(n)
        print(f'english for number: {n}')
        size = len(str(n))
        i = size-1
        output = ''
        temp = 0
        while i >= 0:
            q = n//10**i
            if (i-2)%3 == 0:
                output += f' {self.map[q]} hundred'
            if (i-1)%3 == 0:
                temp = q*10
            if i%3 == 0:
                if temp != 0:
                    if temp+q < 20:
                        output += f' {self.map[temp+q]}'  
                    else:
                        output += f' {self.map[temp]} {self.map[q]}'
                output += f' {self.unit[i]}'
            n = n%10**i
            i -= 1
        print(f'{output}')

if __name__ == '__main__':
    conv = converter()
    conv.toEnglish(631234)