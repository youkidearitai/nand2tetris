#!/usr/bin/env python

import binascii

class JackTokenizer:
    KEYWORD = 0
    SYMBOL = 1
    IDENTIFIER = 2
    INT_CONST = 3
    STRING_CONST = 4

    tokens = []

    keywords = [
        'class',
        'constructor',
        'function',
        'method',
        'field',
        'static',
        'var',
        'int',
        'char',
        'boolean',
        'void',
        'true',
        'false',
        'null',
        'this',
        'let',
        'do',
        'if',
        'else',
        'while',
        'return'
    ]

    symbols = [
        '{',
        '}',
        '(',
        ')',
        '[',
        ']',
        '.',
        ',',
        ';',
        '+',
        '-',
        '*',
        '/',
        '&',
        '|',
        '<',
        '>',
        '=',
        '~'
    ]

    pointer = None
    now_token = ""
    token_type = None

    def __init__(self, fp):
        """
        コンストラクタ
        引数
        fp: 入力ファイル/ストリーム
        """
        self.fp = fp

    def parseEnd(self):
        """
        パース終了
        """
        self.fp.close()

    def hasMoreTokens(self):
        """
        入力にまだトークンは存在するか？
        """
        return self.pointer != ''

    def advance(self):
        """
        入力から次のトークンを取得し
        それを現在のトークンとする。
        hasMoreTokensがtrueの間呼び出す
        最初は現在のトークンを設定していない
        """
        self.pointer = self.fp.read(1)

        if self.pointer in self.symbols:
            self.now_token = self.pointer
            self.token_type = self.SYMBOL
            self.tokens.append(self.now_token)
            self.now_token = ""
            return

        if not self.pointer.isspace():
            self.now_token += self.pointer

        if self.now_token in self.keywords:
            self.token_type = self.KEYWORD
            self.tokens.append(self.now_token)
            self.now_token = ""
            return

        nextChar = self.fp.read(1)
        # eofに到達した場合
        if nextChar == '':
            return

        self.fp.seek(self.fp.tell() - 1, 0)
        if nextChar in self.symbols:
            self.token_type = self.IDENTIFIER
            self.tokens.append(self.now_token)
            self.now_token = ""
            return

        if self.pointer.isdigit():
            self.token_type = self.INT_CONST

            while True:
                self.pointer = self.fp.read(1)

                if not self.pointer.isdigit():
                    break
                else:
                    self.now_token += self.pointer

            self.tokens.append(self.now_token)

            self.fp.seek(self.fp.tell() - 1, 0)
            self.now_token = ""
            return

        if self.pointer == '"':
            self.token_type = self.STRING_CONST
            self.now_token = ""

            while True:
                self.pointer = self.fp.read(1)

                if self.pointer == '"':
                    break
                else:
                    self.now_token += self.pointer

            self.tokens.append(self.now_token)
            self.now_token = ""
            return

        self.token_type = None

    def tokenType(self):
        """
        現トークンの種類を返す
        """
        return self.token_type

    def keyword(self):
        """
        現トークンのキーワードを返す
        これはtokenType()が、KEYWORDのみ呼び出す
        """
        return self.tokens[-1]

    def symbol(self):
        """
        現トークンの文字を返す
        tokenTypeがSYMBOLのみ呼び出す
        """
        return self.tokens[-1]

    def identifier(self):
        """
        現トークンの識別子を返す
        tokenType()がIDENTIFIERの場合のみ呼び出す
        """
        return self.tokens[-1]

    def intVal(self):
        """
        現トークンの整数の値を返す
        tokenType()がINT_CONSTの場合のみ呼び出す
        """
        return int(self.tokens[-1])

    def stringVal(self):
        """
        現トークンの文字列を返す
        tokenType()がSTRING_CONSTの場合のみ呼び出す
        """
        return self.tokens[-1]
