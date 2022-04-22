import random
import re


def imprimeEscolhaUsuario(escolha):
    if escolha == '1':
        print("Você escolheu Pedra")
    elif escolha == '2':
        print("Você escolheu Papel!")
    else:
        print("Você escolheu Tesoura")


def imprimeEscolhaOponente(escolha):
    if escolha == '1':
        print("Eu escolho Pedra")
    elif escolha == '2':
        print("Eu escolho Papel!")
    else:
        print("Eu escolho Tesoura")


def imprimeResultado(escolha_do_usuario, escolha_do_oponente):
    if escolha_do_oponente == escolha_do_usuario:
        print("Empate! ")
    elif escolha_do_usuario == '1' and escolha_do_oponente == '2':
        print("Papel ganha de Pedra, você perdeu!")
    elif escolha_do_usuario == '2' and escolha_do_oponente == '3':
        print("Tesoura ganha de Papel, você perdeu!")
    elif escolha_do_usuario == '3' and escolha_do_oponente == '1':
        print("Pedra ganha de Tesoura, você perdeu!")
    else:
        print("Você ganhou!")


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    continua_jogando = True
    while continua_jogando:
        print("\n")
        print("Pedra, PapeL, Tesoura - Jogue!")
        escolha_do_usuario = input("Escolha sua arma 1-Pedra, 2-Papel, ou 3-Tesoura: ")
        if not re.match("[123]", escolha_do_usuario):
            print("Por favor escolha um número.")
            continue

        choices = ['1', '2', '3']
        escolha_do_oponente = random.choice(choices)

        imprimeEscolhaUsuario(escolha_do_usuario)
        imprimeEscolhaOponente(escolha_do_oponente)
        imprimeResultado(escolha_do_usuario, escolha_do_oponente)

        continua = input("Deseja jogar novamente? 1-Sim ou 2-Não : ")
        if continua == '2':
            continua_jogando = False


if __name__ == "__main__":
    jogar()
