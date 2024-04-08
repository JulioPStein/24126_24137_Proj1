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
            self.arquivinho = open(self._arquivo, "r")
            valores = [self.AnoDaObra, self.MesDaObra, self.Estilo, self.NomeDaObra, self.AutorDaObra, self.ValorEstimado, self.urlFoto]
            linha = "-"
            while linha != "":
                linha = self.arquivinho.readline()
                if linha != "":
                    for valor in valores:
                        valor = linha
                        self.arquivinho.readline()

                    


    def gravarCamposNoArquivo(self):
        if self._abertoParaGravacao:
            self.arquivinho = open(self._arquivo, "a")
            linha = "-"
            valores = [self.AnoDaObra, self.MesDaObra, self.Estilo, self.NomeDaObra, self.AutorDaObra, self.ValorEstimado, self.urlFoto]
            
            for item in valores:
                self.arquivinho.write(f"{item}\n")
            
            


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
    