#!/usr/bin/env python

import glob
import argparse

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Jack Language Analyzer')
    argparser.add_argument('source')
    args = argparser.parse_args()
    print(args.source)
    pass
