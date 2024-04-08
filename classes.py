class Obra():
    def __init__(self):
        self.ano_obra[4] = ""
        self.mes_obra[2] = ""
        self.autor_obra[20] = ""
        self.nome_obra[20] = ""
        self.estilo_obra[15] = ""
        self.url_obra[100] = ""
        self.valor_estimado : float = 0
        self._aberto_para_gravação : bool = 0
        self._arquivo = open(r"")