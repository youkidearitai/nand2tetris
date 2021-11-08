
class CompilationEngine:
    def __init__(self, fp):
        """
        与えられた入力と出力に対して
        新しいコンパイルエンジンを生成する
        次に呼ぶルーチンはcompileClass()でなければならない
        """
        pass

    def compileClass(self):
        """
        クラスをコンパイルする
        """
        pass

    def compileClassVarDec(self):
        """
        スタティック宣言またはフィールド宣言をコンパイルする
        """
        pass

    def compileSubroutine(self):
        """
        メソッド、ファンクション、コンストラクタをコンパイルする
        """
        pass

    def compileParameterList(self):
        """
        パラメータのリストをコンパイルする。()は含まない
        """
        pass

    def compileVarDec(self):
        """
        var宣言をコンパイルする
        """
        pass

    def compileStatements(self):
        """
        一連の文をコンパイルする。波括弧は含まない
        """
        pass

    def compileDo(self):
        """
        do文をコンパイルする
        """
        pass

    def compileLet(self):
        """
        Let文をコンパイルする
        """
        pass

    def compileWhile(self):
        """
        while文をコンパイルする
        """
        pass

    def compileReturn(self):
        """
        return文をコンパイルする
        """
        pass

    def compileIf(self):
        """
        If文をコンパイルする
        """
        pass

    def compileExpression(self):
        """
        式をコンパイルする
        """
        pass

    def compileTerm(self):
        """
        termをコンパイルする
        先読みなどがある
        """
        pass

    def compileExpressionList(self):
        """
        コンマで分離された式のリストをコンパイルする
        """
        pass
        
