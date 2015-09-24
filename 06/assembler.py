#!/usr/bin/env python3.4

import parser
import code

filename = 'test.asm'

p = parser.Parser(open(filename, 'r'))
c = code.Code()

while True:
    binary = 0b0000000000000000

    line = p.advance()

    if p.hasMoreCommands() != True:
        break

    command_type = p.commandType()

    if command_type == parser.C_COMMAND:
        binary = binary + (0b111 << 13)
        binary = binary + (c.comp(p.comp()) << 6)
        binary = binary + (c.dest(p.dest()) << 3)
        binary = binary + c.jump(p.jump())

    print(bin(binary))


