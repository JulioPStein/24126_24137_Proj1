class Obra:
    def __init__(self, nomeArq : str, paraGravacao : bool):
        self.AnoDaObra = ""
        self.MesDaObra = ""
        self.AutorDaObra = ""
        self.NomeDaObra = ""
        self.Estilo = ""
        self.ValorEstimado = 0.0
        self.urlFoto = ""
        self.arquivvo = ""
        self._arquivo = nomeArq
        self._abertoParaGravacao = paraGravacao

    @property
    def PodeGravar(self):
        return self._abertoParaGravacao
    
    @property
    def Arquivo(self):
        return self._arquivo

    def lerCamposDoArquivo(self):
        if not self._abertoParaGravacao:
            # arrumar
            self.arquivinho = open(self._arquivo, "r")
            self.linha = self.arquivinho.readline()
            self.AnoDaObra = self.linha[:4].rstrip()
            self.MesDaObra = self.linha[7:9].rstrip()
            self.AutorDaObra = self.linha[53:73].strip()
            self.NomeDaObra = self.linha[30:50].strip()
            self.Estilo = self.linha[12:27].rstrip()
            self.ValorEstimado = None           #ver como pegar apenas o valor estimado e colocar em uma vaiável
            self.urlFoto = None             


    def gravarCamposNoArquivo(self):
        # arrumar
        if self._abertoParaGravacao:
            self.arquivinho = open(self._arquivo, "a")
            self.linha = self.AnoDaObra.ljust(4, " ") + "   " + self. MesDaObra.ljust(2, " ") + "   " + self.Estilo.ljust(15, " ") + "   " + self.NomeDaObra.ljust(20, " ") + "   " + self.AutorDaObra.ljust(20, " ") + "   " + self.ValorEstimado + "    " + self.urlFoto
            self.arquivinho.write(f"\n{self.linha}")
            


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
        self.arquivinho.close()

    def __str__(self) -> str:
        pass

    def compararCom(self, outraObra, Obra) -> int:
        pass
    