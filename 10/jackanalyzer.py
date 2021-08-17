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
        print(jk)
