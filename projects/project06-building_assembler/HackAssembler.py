from Parser import Parser
from Code import Code
from SymbolTable import SymbolTable
import sys

# assembly_file, hack_file = sys.argv[1], sys.argv[2]
assembly_file, hack_file = './rect/RectL.asm', './rect/RectL.hack'

asm = open(assembly_file)
hack = open(hack_file, 'w')
line_number = 0
lines = []
symbol_table = SymbolTable()
code = Code()

def count_line(parsed_type):
    global line_number

    if parsed_type == 'a' or parsed_type == 'c':
        line_number += 1

# first pass
for line in asm:
    parsed_line = Parser(line).get_parsed()

    if not parsed_line:
        continue

    parsed_type = parsed_line['type']
    count_line(parsed_type)

    if parsed_type == 'l':
        label = parsed_line['label']
        symbol_table.add_label(label, line_number)

    lines.append(line)

# second pass
for i, line in enumerate(lines):
    parsed_line = Parser(line).get_parsed()

    if not parsed_line:
        continue

    parsed_type = parsed_line['type']

    if parsed_type == 'l':
        continue

    elif parsed_type == 'c':
        hack_code = code.translate_c_inst(parsed_line)
    
    elif parsed_type == 'a':
        parsed_value = parsed_line['value']
        converted_value = symbol_table.lookup(parsed_value)
        hack_code = '0' + code.translate_a_inst(converted_value)
    
    if i != (len(lines) - 1):
        hack.write(hack_code + '\n')
    
    else:
        hack.write(hack_code)

asm.close()
hack.close()