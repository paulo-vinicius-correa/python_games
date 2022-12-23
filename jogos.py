import forca
import adivinhacao

def escolha_seu_jogo():
    print("*********************************")
    print("********Escolha seu jogo!********")
    print("*********************************")

    print("(1) Jogo da Forca (2) Jogo de Adivinhação")

    jogo = int(input("Qual o jogo escolhido?"))
    print("Você Escolheu " , jogo)

    if(jogo == 1):
        print("iniciando jogo da Forca...")
        forca.jogar()
    elif(jogo == 2):
        print("iniciando jogo de adivinhação")
        adivinhacao.jogar ()

if(__name__ == "__main__"):
    escolha_seu_jogo()


    