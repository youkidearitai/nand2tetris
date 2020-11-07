#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vm_parser
import codewriter
import sys
import os
import glob

def compileFile(filename):
  f = open(filename, 'r', encoding="utf-8")
  p = vm_parser.Parser(f)
  fileSymbol = filename.split(".")[0]
  output_file_name = fileSymbol + ".asm"
  o = open(output_file_name, 'w', encoding="utf-8")
  c = codewriter.CodeWriter(o)
  c.setFileName(os.path.basename(fileSymbol))

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


def main():
  if len(sys.argv) < 2:
    print("usage: python vmtranslator.py filename")
    return

  filename = sys.argv[1]

  if filename.endswith(".vm"):
      vms = [filename]
  else:
      # ディレクトリなどの場合は複数コンパイルを試みる
      vms = glob.glob("{0}/*.vm".format(os.path.dirname(filename)))

  for vm in vms:
      compileFile(vm)

if __name__ == '__main__':
  main()
