#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vm_parser
import codewriter
import sys
import os
import glob

def compileFile(filename, destination, o):
  f = open(filename, 'r', encoding="utf-8")
  p = vm_parser.Parser(f)
  fileSymbol = filename.split(".")[0]

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
  destination = filename.split(".")[0]

  if filename.endswith(".vm"):
      vms = [filename]

      output_file_name = filename.split('.')[0] + ".asm"
      output_file = open(output_file_name, 'w', encoding="utf-8")
  else:
      # ディレクトリなどの場合は複数コンパイルを試みる
      vms = glob.glob("{0}/*.vm".format(os.path.dirname(filename)))

      output_file_name = os.path.split(filename.strip('/'))[-1].split('.')[0] + ".asm"
      output_file = open(destination + output_file_name, 'w', encoding="utf-8")

  for vm in vms:
      compileFile(vm, destination, output_file)

if __name__ == '__main__':
  main()
