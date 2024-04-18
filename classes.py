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
        if self._aberto_para_gravação:
            self._arquivo = open(nomeArq, "a")
        else:
            self._arquivo = open(nomeArq, "r")
    
    def lerCamposDoArquivo(self):
        if not self._aberto_para_gravação:
            file = self._arquivo.readline()
            self.preencherCampos()

    def gravarCamposNoArquivo(self):
        if self._aberto_para_gravação:
            self._arquivo.write(self.__str__())

    def preencherCampos(self, novoAno, novoMes, novoEstilo, novoNome, novoAutor, novaURL : str, novoValor):
        self.ano_obra = novoAno
        self.mes_obra = novoMes
        self.autor_obra = novoAutor
        self.nome_obra = novoNome
        self.estilo_obra = novoEstilo
        self.valor_estimado = novoValor
        self.url_obra = novaURL

    def fecharArquivo(self):
        self._arquivo.close()

    def __str__(self) -> str:
        string = "{self.ano_obra.rjust(4, " ")} {self.mes_obra.rjust(2, " ")} {self.estilo_obra.rjust(20, " ")} {self.nome_obra.rjust(20, " ")} {self.autor_obra.rjust(15, " ")} {str(self.valor_estimado).rjust(10, " ")} {self.url_obra.rjust(100, " ")}"
        return string

    def compararCom(self):
        pass