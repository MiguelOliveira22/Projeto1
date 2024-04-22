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
            if file == "":
                return 1
            self.preencherCampos(file[0:4], file[6:8], file[10:25], file[27:47], file[49:69], file[71:81], file[83:183])

    def gravarCamposNoArquivo(self):
        if self._aberto_para_gravação:
            self._arquivo.write(f"{self.__str__()}" + "\n")

    def preencherCampos(self, novoAno, novoMes, novoEstilo, novoNome, novoAutor, novoValor, novaURL : str):
        self.ano_obra = novoAno[0:4]
        self.mes_obra = novoMes[0:2]
        self.autor_obra = novoAutor[0:20]
        self.nome_obra = novoNome[0:20]
        self.estilo_obra = novoEstilo[0:15]
        self.valor_estimado = float(novoValor)
        self.url_obra = novaURL[0:100]

    def fecharArquivo(self):
        self._arquivo.close()

    def __str__(self) -> str:
        valor = f"{self.valor_estimado:.2f}"
        string = f"{self.ano_obra.rjust(4)}  {self.mes_obra.rjust(2)}  {self.estilo_obra.ljust(15)}  {self.nome_obra.ljust(20)}  {self.autor_obra.ljust(20)}  {valor.rjust(10)}  {self.url_obra.ljust(100)}"
        return string

    def compararCom(self):
        pass