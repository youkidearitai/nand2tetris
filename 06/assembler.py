#!/usr/bin/env python3.4

import parser
import code
import sys
import re

if len(sys.argv) < 2:
    print("usage: python assembler.py filename")

f = open(sys.argv[1], 'r')
p = parser.Parser(f)
c = code.Code()

isint = re.compile("^[0-9]+$")

output_file_name = sys.argv[1].split(".")[0] + ".hack"
output_file = open(output_file_name, 'w')

while True:
    binary = 0b0000000000000000

    line = p.advance()

    if p.hasMoreCommands() != True:
        break

    command_type = p.commandType()
    if command_type is None:
        continue

    if command_type == parser.C_COMMAND:
        binary = binary + (0b111 << 13)
        binary = binary + (c.comp(p.comp()) << 6)
        binary = binary + (c.dest(p.dest()) << 3)
        binary = binary + c.jump(p.jump())

    if command_type == parser.A_COMMAND:
        symbol = p.symbol()
        if isint.search(symbol):
            binary = binary + int(symbol)

    write_line = "{0:0>16}".format(format(binary, 'b'))
    output_file.write(write_line + "\n")

output_file.close()
f.close()


