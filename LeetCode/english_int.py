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
            6 : 'million',
            9 : 'billion',
            12: 'trillion'
        }

    def toEnglish(self, n):
        size = len(str(n))
        i = size-1
        output = ''
        temp = 0
        value = False
        while i >= 0:            
            q = n//10**i
            #verifico l'esistenza di valori in questa tripletta
            if q > 0:
                value = True
            if (i-2)%3 == 0 and q != 0:
                output += f'{self.map[q]} hundred '
            elif (i-1)%3 == 0:
                temp = q*10
            elif i%3 == 0:
                if temp != 0:
                    if temp+q <= 20:
                        output += f'{self.map[temp+q]} '  
                    elif q != 0:
                        output += f'{self.map[temp]} {self.map[q]} '
                    else:
                        output += f'{self.map[temp]} '
                elif (q == 0 and i == 0 and size == 1) or q!=0:
                    output += f'{self.map[q]} '

                if i != 0 and value:
                    output += f'{self.unit[i]} '
                    value = False
            n = n%10**i
            i -= 1
        return output