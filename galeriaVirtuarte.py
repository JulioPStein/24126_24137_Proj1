class Obra:
    def __init__(self, nomeArq : str, paraGravacao : bool):
        self.AnoDaObra = ""
        self.MesDaObra = ""
        self.AutorDaObra = ""
        self.NomeDaObra = ""
        self.Estilo = ""
        self.ValorEstimado = 0.0 # 12 caracteres
        self.urlFoto = ""
        self.arquivinho = ""
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
            lista = []
            self.arquivo = open(self._arquivo, "r")
            self.linha = self.arquivo.readline()    
            while self.linha != "":
                self.linha = self.arquivo.readline()
                self.AnoDaObra = self.linha[:4].rstrip()
                self.MesDaObra = self.linha[4:6].rstrip()
                self.Estilo = self.linha[6:21].rstrip()
                self.NomeDaObra = self.linha[21:41].rstrip()
                self.AutorDaObra = self.linha[41:61].rstrip()
                self.ValorEstimado = self.linha[61:73].replace(" ", "")
                self.urlFoto = self.linha[73:173].rstrip()
                lista.append(str(self.AnoDaObra + self.MesDaObra + self.Estilo + self.NomeDaObra + self.AutorDaObra + str(self.ValorEstimado) + self.urlFoto))

            return lista


    def gravarCamposNoArquivo(self):
        if self._abertoParaGravacao:
            self.arquivo = open(self._arquivo, "a")
            self.linha = self.AnoDaObra.ljust(4, " ") + self. MesDaObra.ljust(2, " ") + self.Estilo.ljust(15, " ") + self.NomeDaObra.ljust(20, " ") + self.AutorDaObra.ljust(20, " ") + str(self.ValorEstimado).ljust(12, " ") + self.urlFoto.ljust(100, " ")
            self.arquivo.write(f"\n{self.linha}")


    def preencherCampos(self, novoAno, novoMes, novoAutor, novoNome, novoEstilo, novoValor, novaURL : str):
        if self._abertoParaGravacao:
            self.AnoDaObra = novoAno
            self.MesDaObra = novoMes
            self.AutorDaObra = novoAutor
            self.NomeDaObra = novoNome
            self.Estilo = novoEstilo
            self.ValorEstimado = novoValor
            self.urlFoto = novaURL

    def __str__(self) -> str:
        resultado =  self.AnoDaObra + self.MesDaObra + self.Estilo + self.NomeDaObra + self.AutorDaObra + str(self.ValorEstimado) + self.urlFoto    

    def fecharArquivo(self):
        self.arquivo.close()



    def compararCom(self, outraObra, Obra) -> int:
        pass
    