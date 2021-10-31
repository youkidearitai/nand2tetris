#!/usr/bin/env python

import glob
import argparse
import jacktokenizer

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Jack Language Analyzer')
    argparser.add_argument('source')
    args = argparser.parse_args()
    for src in glob.glob(args.source):
        fp = open(src)
        jk = jacktokenizer.JackTokenizer(fp)
        tokens = []
        while jk.hasMoreTokens():
            jk.advance()

            tokenType = jk.tokenType()
            if tokenType == jk.KEYWORD:
                tokens.append(jk.keyword())
            elif tokenType == jk.SYMBOL:
                tokens.append(jk.symbol())
            elif tokenType == jk.IDENTIFIER:
                tokens.append(jk.identifier())
            elif tokenType == jk.INT_CONST:
                tokens.append(jk.intVal())
            elif tokenType == jk.STRING_CONST:
                tokens.append(jk.stringVal())


    print(jk.tokens)
    print(tokens)
    jk.parseEnd()
    print("End Analyze.")
