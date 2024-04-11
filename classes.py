class Obra():
    def __init__(self, nomeArq : str, paraEscrever : bool):
        self.ano_obra : str[4] = ""
        self.mes_obra : str[2] = ""
        self.autor_obra : str[20] = ""
        self.nome_obra : str[20] = ""
        self.estilo_obra : str[15] = ""
        self.url_obra : str[100] = ""
        self.valor_estimado : float = 0
        self._aberto_para_gravação : bool = paraEscrever
        self._arquivo : str = nomeArq
    
    def lerCamposDoArquivo(self):
        if not self._aberto_para_gravação:
            file = open(repr(self._arquivo), "r")
            a = file.readline()
            file.close()

    def gravarCamposNoArquivo(self):
        if self._aberto_para_gravação:
            file = open(repr(self._arquivo), "a")
            file.write(self.__str__())
            file.close()

    def preencherCampos(self, novoAno, novoMes, novoAutor, novoNome, novoEstilo, novoValor, novaURL : str):
        self.ano_obra = novoAno
        self.mes_obra = novoMes
        self.autor_obra = novoAutor
        self.nome_obra = novoNome
        self.estilo_obra = novoEstilo
        self.valor_estimado = novoValor
        self.url_obra = novaURL

    def fecharArquivo(self):
        pass

    def __str__(self):
        string = ""
        return string

    def compararCom(self):
        pass