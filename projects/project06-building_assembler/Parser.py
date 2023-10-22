class Parser:
    def __init__(self, instruction):
        instruction = self.comment_reducer(instruction.strip())
        if (not instruction) or (instruction[0] == '//'):
            self.type = None
        elif instruction[0] == '(':
            self.parse_l_inst(instruction)
        elif instruction[0] == '@':
            self.parse_a_inst(instruction)
        else:
            self.parse_c_inst(instruction)
    
    def comment_reducer(self, string):
        return string.split('//')[0].strip()
    
    def parse_l_inst(self, instruction):
        self.type = 'l'
        self.label = instruction.strip("()")
    
    def parse_a_inst(self, instruction):
        self.type = 'a'
        self.value = instruction[1:]

    def parse_c_inst(self, instruction):
        self.type = 'c'
        split_inst0 = instruction.split(';')

        if len(split_inst0) == 1:
            self.jump = 'null'
        
        else:
            self.jump = split_inst0[1]
        
        split_inst1 = split_inst0[0].split('=')

        if len(split_inst1) == 1:
            self.dest = 'null'
            self.comp = split_inst1[0]
        
        else:
            self.dest = split_inst1[0]
            self.comp = split_inst1[1]
        
    
    def get_parsed(self):
        if self.type == 'a':
            return { 'type': self.type, 'value': self.value }
        
        elif self.type == 'l':
            return { 'type': self.type, 'label': self.label }

        elif self.type == 'c':
            return { 'type': self.type, 'comp': self.comp, 'dest': self.dest, 'jump': self.jump }
        
        else:
            return None