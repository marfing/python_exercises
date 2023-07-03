#hashtable.py


#usato per inizializzare i valori di una ash table vuota
#così da poter inserire anche None come valore valido in seguito
BLANK = object()

class HashTable:
    def __init__(self, capacity) -> None:
        self.values = capacity * [BLANK]

    def __len__(self) -> int:
        return len(self.values)
    
    def __setitem__(self, key, value):
        #come resto posso sempre e solo avere valori tra 0 e capacity-1
        index = hash(key) % len(self)
        self.values[index] = value

    def __getitem__(self, key):
        index = hash(key) % len(self)
        if self.values[index] is BLANK:
            #print('raising KeyError')
            raise KeyError(key)
        return self.values[index]
    

    