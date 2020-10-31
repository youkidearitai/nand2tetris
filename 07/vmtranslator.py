#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vm_parser
import codewriter
import sys

def main():
  if len(sys.argv) < 2:
    print("usage: python vmtranslator.py filename")
    return

  f = open(sys.argv[1], 'r')
  p = vm_parser.Parser(f)
  output_file_name = sys.argv[1].split(".")[0] + ".asm"
  o = open(output_file_name, 'w')
  c = codewriter.CodeWriter(o)

  while True:
    p.advance()
    if p.hasMoreCommands() != True:
      break

    try:
      command_type = p.commandType()
    except vm_parser.NotCommandErrorException:
      continue

    if command_type == vm_parser.C_ARITHMETIC:
      c.writeArithmetic(p.arg1())

    if command_type == vm_parser.C_PUSH:
      c.writePushpop("push", p.arg1(), p.arg2())

    if command_type == vm_parser.C_POP:
      c.writePushpop("pop", p.arg1(), p.arg2())

if __name__ == '__main__':
  main()

