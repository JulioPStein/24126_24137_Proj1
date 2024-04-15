#arquivo insano
import os
import tkinter as tk

root = tk.Tk()
root.withdraw()
root.attributes("-topmost", True)

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
                case "3" : tabelaHtml()
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
            
            novoAno = input("Ano da conclusão da obra : ")
            
            if novoAno != "0":
                if len(novoAno) < 4:
                    novoAno = novoAno.rjust(4, "0")
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
        valorTotal += float(linha[67:79].rstrip())
        numObras += 1
    print(f"                 Número de obras: {numObras}                         Valor: {valorTotal:12.2f}\n")

    obra.fecharArquivo()
    input("pressione [enter] para continuar")
    os.system('cls') or None

def tabelaHtml():
    from tkinter import filedialog
    import galeriaVirtuarte, webbrowser

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

    file_path = "obras.html"
    html_string = f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <link rel="stylesheet" href="styleObras.css">
</head>

<body>

    <table>
        <tr>
            <th colspan="6">
                RELATÓRIO DE OBRAS DA GALERIA VIRTUAL
            </th>
        </tr>

        <tr>
            <td>Ano/Mês</td>
            <td>Dados</td>
            <td>Estilo</td>
            <td>Autor</td>
            <td>Valor</td>
            <td>Imagem</td>
        </tr>

"""

    obra = galeriaVirtuarte.Obra(nomeDoArquivo, paraGravacao=False)
    totalGeral = 0.0
    totalAno = 0.0
    anoAtual = 0
    primeiraVez = True

    for linha in obra.lerCamposDoArquivo():
        ano = linha[0, 4]
        mes = linha[5, 7]
        estilo = linha[9, 24]
        nomeObra = linha[25, 45]
        autor = linha[46, 66]
        valor = linha[67, 79]
        url = linha[80, 180]

        ano = tirar0s(ano)

        totalAno += float(linha[67:79].rstrip())
        totalGeral += float(linha[67:79].rstrip())
        if primeiraVez == True:
            anoAtual = ano
            primeiraVez = False
        
        if ano != anoAtual:
            html_file = html_file + f"""        <tr>
    <td colspan="4">Total</td>
    <td>{totalAno:12.2f}</td>
</tr>
"""
            totalAno = 0.0
        html_file = html_file + f"""        <tr>
    <td>{ano} / {mes}</td>
    <td>{nomeObra}</td>
    <td>{estilo}</td>
    <td>{autor}</td>
    <td>{valor}</td>
    <td><img src="{url}" alt="{url}"></td>
"""

    html_file = html_file + f"""</body>
</html>"""


    with open(file_path, 'w', encoding="utf-8") as html_file:
        html_file.write(html_string)
    webbrowser.open_new_tab(file_path)
    html_file.close()

def TrianguloPascal():
    import mat
    valorBase = int(input("Digite o valor da base: "))
    tri = mat.Matematica(valorBase)

    for linha in tri.triangulo_de_Pascal():
        print(linha)

    input("pressione [enter] para continuar")
    os.system('cls') or None
        
def tirar0s(ano):
    anoTaOk = False
    while anoTaOk == False:
        if ano[0] == 0:
            ano.replace("0", "", 1)
        else:
            anoTaOk = True
    return ano

if __name__ == "__main__":
    SeletorDeOpcoes()
#1987 09  gamer           VICTORY ROYALE       Vinicius games       9999.00      qliuwsgdf -----exemplo de string concatenada na lista