class Obra():
    def __init__(self):
        self.ano_obra : str[4] = ""
        self.mes_obra : str[2] = ""
        self.autor_obra : str[20] = ""
        self.nome_obra : str[20] = ""
        self.estilo_obra : str[15] = ""
        self.url_obra : str[100] = ""
        self.valor_estimado : float = 0
        self._aberto_para_gravação : bool = 0
        self._arquivo = 0
    
    def lerCamposDoArquivo(self):
        pass

    def gravarCamposNoArquivo(self):
        pass

    def preencherCampos(self):
        pass

    def fecharArquivo(self):
        pass

    def __str__(self):
        pass