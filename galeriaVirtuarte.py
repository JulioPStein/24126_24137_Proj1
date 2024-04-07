class Obras:
    def __init__(self, nomeArq : str, paraGravacao : bool):
        self.AnoDaObra = ""
        self.MesDaObra = ""
        self.AutorDaObra = ""
        self.NomeDaObra = ""
        self.ValorEstimado = 0.0
        self.urlFoto = ""
        self._arquivo = nomeArq
        self._abertoParaGravacao = paraGravacao

    def lerCamposDoArquivo(self):
        pass

    def gravarCamposNoArquivo(self):
        pass

    def preencherCampos(self, novoAno, novoMes, novoAutor, novoNome, novoEstilo, novoValor, novaURL : str):
        pass

    def fecharArquivo(self):
        pass

    def __str__(self) -> str:
        pass

    def compararCom(self, outraObra, Obra) -> int:
        pass
    