class Obra:
    def __init__(self, nomeArq : str, paraGravacao : bool):
        self.AnoDaObra = ""
        self.MesDaObra = ""
        self.AutorDaObra = ""
        self.NomeDaObra = ""
        self.Estilo = ""
        self.ValorEstimado = 0.0 # 12 caracteres
        self.urlFoto = ""
        self.arquivo = ""
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
            import os
            comando = f'sort {self._arquivo} /o ordenado.txt /+1'
            os.system(comando) or None
            lista = []
            self.arquivo = open("ordenado.txt", "r")
            linha = "-"  
            while linha != "":
                linha = self.arquivo.readline()
                if linha != "":
                    self.AnoDaObra = linha[:4]
                    self.MesDaObra = linha[4:6]
                    self.Estilo = linha[6:21]
                    self.NomeDaObra = linha[21:41]
                    self.AutorDaObra = linha[41:61]
                    self.ValorEstimado = f"{float(linha[61:73].strip()):12.2f}"
                    self.urlFoto = linha[73:173]
                    lista.append(str(self.AnoDaObra + " " + self.MesDaObra + "  " + self.Estilo + " " + self.NomeDaObra + " " + self.AutorDaObra + " " + str(self.ValorEstimado.lstrip().ljust(12, " ")) + " " + self.urlFoto))
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



    def compararCom(self, outraObra : str) -> int:
        tamanho1 = len(self.AnoDaObra + self.MesDaObra + self.AutorDaObra + self.NomeDaObra)
        tamanho2 = len(outraObra)
        if tamanho1 < tamanho2:
            return -1
        elif tamanho1 == tamanho2:
            return 0
        else:
            return 1
    