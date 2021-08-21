#!/usr/bin/env python

class JackTokenizer:
    KEYWORD = 0
    SYMBOL = 1
    IDENTIFIER = 2
    INT_CONST = 3
    STRING_CONST = 4

    tokens = []

    pointer = None

    def __init__(self, fp):
        """
        コンストラクタ
        引数
        fp: 入力ファイル/ストリーム
        """
        self.fp = fp

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

    def tokenType(self):
        """
        現トークンの種類を返す
        """
        return self.KEYWORD

    def keyword(self):
        """
        現トークンのキーワードを返す
        これはtokenType()が、KEYWORDのみ呼び出す
        """
        return 0

    def symbol(self):
        """
        現トークンの文字を返す
        tokenTypeがSYMBOLのみ呼び出す
        """
        return ""

    def identifier(self):
        """
        現トークンの識別子を返す
        tokenType()がIDENTIFIERの場合のみ呼び出す
        """
        return ""

    def intVal(self):
        """
        現トークンの整数の値を返す
        tokenType()がINT_CONSTの場合のみ呼び出す
        """
        return 0

    def stringVal(self):
        """
        現トークンの文字列を返す
        tokenType()がSTRING_CONSTの場合のみ呼び出す
        """
        return ""
