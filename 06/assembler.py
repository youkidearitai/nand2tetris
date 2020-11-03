#!/usr/bin/env python3.4

import asm_parser
import code
import sys
import re
import symboltable

if len(sys.argv) < 2:
    print("usage: python assembler.py filename")

f = open(sys.argv[1], 'r')
p = asm_parser.Parser(f)
c = code.Code()

isint = re.compile("^[0-9]+$")

s = symboltable.SymbolTable()
address = 0

while True:
    binary = 0b0000000000000000
    line = p.advance()

    if p.hasMoreCommands() != True:
        break

    command_type = p.commandType()
    if command_type is None:
        continue

    if command_type == asm_parser.L_COMMAND:
        s.addEntity(p.symbol(), address)

    if command_type == asm_parser.A_COMMAND or command_type == asm_parser.C_COMMAND:
        address = address + 1

f.seek(0)
p = asm_parser.Parser(f)

output_file_name = sys.argv[1].split(".")[0] + ".hack"
output_file = open(output_file_name, 'w')

variable_address = 16

while True:
    binary = 0b0000000000000000

    line = p.advance()

    if p.hasMoreCommands() != True:
        break

    command_type = p.commandType()
    if command_type is None:
        continue

    if command_type == asm_parser.L_COMMAND:
        continue

    if command_type == asm_parser.C_COMMAND:
        binary = binary + (0b111 << 13)
        binary = binary + (c.comp(p.comp()) << 6)
        binary = binary + (c.dest(p.dest()) << 3)
        binary = binary + c.jump(p.jump())

    if command_type == asm_parser.A_COMMAND:
        symbol = p.symbol()
        if isint.search(symbol):
            binary = binary + int(symbol)
        elif s.contains(symbol):
            binary = binary + s.getAddress(symbol)
        else:
            s.addEntity(symbol, variable_address)
            binary = variable_address
            variable_address = variable_address + 1

    write_line = "{0:0>16}".format(format(binary, 'b'))
    output_file.write(write_line + "\n")

output_file.close()
f.close()


