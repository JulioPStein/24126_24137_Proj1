class Obra:
    def __init__(self, nomeArq : str, paraGravacao : bool):
        self.AnoDaObra = ""
        self.MesDaObra = ""
        self.AutorDaObra = ""
        self.NomeDaObra = ""
        self.Estilo = ""
        self.ValorEstimado = 0.0
        self.urlFoto = ""
        self._arquivo = nomeArq
        self._abertoParaGravacao = paraGravacao

    @property
    def PodeGravar(self):
        return self._abertoParaGravacao
    
    @property
    def Arquivo(self):
        return self._arquivo

    def lerCamposDoArquivo(self):
        pass

    def gravarCamposNoArquivo(self):
        if self._abertoParaGravacao:
            arquivo = open(self._arquivo, "a")
            self.linha = self.AnoDaObra.ljust(4, " ") + "   " + self. MesDaObra.ljust(2, " ") + "   " + self.Estilo.ljust(15, " ") + "   " + self.NomeDaObra.ljust(20, " ") + "   " + self.AutorDaObra.ljust(20, " ") + "   " + self.ValorEstimado + "   " + self.urlFoto
            arquivo.write(f"\n{self.linha}")


    def preencherCampos(self, novoAno, novoMes, novoAutor, novoNome, novoEstilo, novoValor, novaURL : str):
        if self._abertoParaGravacao:
            self.AnoDaObra = novoAno
            self.MesDaObra = novoMes
            self.AutorDaObra = novoAutor
            self.NomeDaObra = novoNome
            self.Estilo = novoEstilo
            self.ValorEstimado = novoValor
            self.urlFoto = novaURL



    def fecharArquivo(self):
        pass

    def __str__(self) -> str:
        pass

    def compararCom(self, outraObra, Obra) -> int:
        pass
    