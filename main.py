#arquivo insano
import os

def AcoesPossiveis():
    print("\n\nCadastro de obras de arte .........1")
    print("Listagem de obras de arte .........2")
    print("Pagina web com obras de arte ......3")
    print("Triângulo de Pascal ...............4")
    print("Terminar a execução do programa ...0")


def SeletorDeOpcoes():
    
    acao = "-"
    while acao != "0":
        os.system("cls") or None
        AcoesPossiveis()
        acao = input("\nDigite o número referente à ação desejada: ")
        valorinvalido = "-"
        if acao != "0" and acao != "1" and acao != "2" and acao != "3" and acao != "4":
            print("Opção inválida")
            input("Digite [enter] para continuar")
        else:
            match acao:
                case "0" : Terminar()
                case "1" : Cadastro() 
                case "2" : Listagem()
                case "3" : pass
                case "4" : TrianguloPascal()

def Terminar():
    print("Obrigado pelo uso!")
    print("Saindo da memória.")
    input("Digite [enter] para terminar")
    os.system("cls") or None

def Cadastro():
    from tkinter import filedialog
    import galeriaVirtuarte

    tiposDeArquivos = (   #VER SE SÃO ESSES  OS TIPOS DESEJADOS
        ("Arquivos de texto", "*.txt"),
        ("Arquivos JSON", "*.json"),
        ("Qualquer arquivo", "*.*")
    )

    nomeDoArquivo = filedialog.askopenfilename(
        title="Selecione o arquivo desejado",
        initialdir= r"c:\temp",
        multiple = False,
        filetypes = tiposDeArquivos
    )
    if nomeDoArquivo != "":
        novoAno = "-"
        while novoAno != "0":

            if novoAno == "-":
                print("\nDados da obra")
            else:
                print("Adicionar nova obra")
                print("Digite 0 na pergunta abaixo para sair")
            
            novoAno = input("Ano da conclusão da obra: ")
            
            if novoAno != "0":
                novoMes = input("Mês da conclusão da obra: ")
                novoAutor = input("Autor da obra: ")
                novoNome = input("Nome da obra: ")
                novoEstilo = input("Estilo da obra: ")
                novoValor = input("Valor da obra: ")
                novaURL = input("Url da foto: ")

                obra = galeriaVirtuarte.Obra(nomeDoArquivo, paraGravacao=True)

                obra.preencherCampos(novoAno, novoMes, novoAutor, novoNome, novoEstilo, novoValor, novaURL)

                obra.gravarCamposNoArquivo()

                print("\nObra adicionada com sucesso")
                input("pressione [enter] para continuar")
                os.system('cls') or None

        obra.fecharArquivo()   

def Listagem():
    from tkinter import filedialog
    import galeriaVirtuarte

    tiposDeArquivos = (   #VER SE SÃO ESSES  OS TIPOS DESEJADOS
        ("Arquivos de texto", "*.txt"),
        ("Arquivos JSON", "*.json"),
        ("Qualquer arquivo", "*.*")
    )

    nomeDoArquivo = filedialog.askopenfilename(
        title="Selecione o arquivo desejado",
        initialdir= r"c:\temp",
        multiple = False,
        filetypes = tiposDeArquivos
    )

    obra = galeriaVirtuarte.Obra(nomeDoArquivo, paraGravacao=False)
    valorTotal = 0.0
    numObras = 0
    print("Ano  Mes Estilo          Nome da Obra         Autor da Obra        Valor        Url")
    for linha in obra.lerCamposDoArquivo():
        print(linha)
        valorTotal += float(linha[61:73].rstrip())
        numObras += 1
    print(f"                 Número de obras: {numObras}                         Valor: {valorTotal:12.2f}\n")

    obra.fecharArquivo()
    input("pressione [enter] para continuar")
    os.system('cls') or None


def TrianguloPascal():
    import mat
    valorBase = int(input("Digite o valor da base: "))
    tri = mat.Matematica(valorBase)

    for linha in tri.triangulo_de_Pascal():
        print(linha)

    input("pressione [enter] para continuar")
    os.system('cls') or None
        

if __name__ == "__main__":
    SeletorDeOpcoes()
