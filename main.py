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
        acao = input("\nDigite o número referente à ação desejada:")


while __name__ == "__main__":
    SeletorDeOpcoes()
