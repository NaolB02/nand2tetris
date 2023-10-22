class SymbolTable:
    def __init__(self) -> None:
        self.table = {
            'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5, 'R6': 6, 'R7': 7,
            'R8': 8, 'R9': 9, 'R10': 10, 'R11': 11, 'R12': 12, 'R13': 13, 'R14': 14, 'R15': 15,
            'SCREEN': 16384, 'KBD': 24576, 'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4
        }

        self.cur_available_memory = 16
    
    def lookup(self, value):
        if value.isnumeric():
            return int(value)
        
        elif value in self.table:
            return self.table[value]

        else:
            self.table[value] = self.cur_available_memory
            self.cur_available_memory += 1
            return self.table[value]
        
    def add_label(self, label, num=0):
        self.table[label] = num