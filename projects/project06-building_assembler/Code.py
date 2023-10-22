class Code:
    def __init__(self):
        self.comp_table = {
            '0': '0101010', '1': '0111111', '-1':'0111010', 'D':'0001100', 'A': '0110000', '!D': '0001101',
            '!A': '0110001', '-D': '0001111', '-A': '0110011', 'D+1': '0011111', 'A+1': '0110111','D-1': '0001110',
            'A-1': '0110010', 'D+A': '0000010', 'D-A': '0010011', 'A-D':'0000111','D&A': '0000000', 'D|A': '0010101',
            'M': '1110000', '!M': '1110001', '-M': '1110011', 'M+1': '1110111', 'M-1': '1110010', 'D+M': '1000010',
            'D-M': '1010011', 'M-D': '1000111','D&M': '1000000', 'D|M': '1010101'
            }
        
        self.dest_table = {
            'null':'000', 'M':'001', 'D':'010',
            'DM':'011', 'MD':'011', 'A':'100',
            'AM':'101', 'MA':'101', 'AD':'110',
            'DA':'110', 'ADM':'111', 'MAD':'111',
            'AMD':'111', 'MDA':'111', 'DMA':'111',
            'DAM':'111'
        }

        self.jump_table = {
            'null':'000', 'JGT':'001', 'JEQ':'010',
            'JGE':'011', 'JLT':'100', 'JNE':'101',
            'JLE':'110', 'JMP':'111'
        }
    
    def translate_c_inst(self, parsed):
        initial = '111'
        comp = self.comp_table[parsed['comp']]
        dest = self.dest_table[parsed['dest']]
        jump = self.jump_table[parsed['jump']]

        return initial + comp + dest + jump

    def translate_a_inst(self, value):
        return '{0:015b}'.format(value)