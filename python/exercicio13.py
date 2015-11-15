#!/usr/bin/env python3
"""
Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule
seu peso ideal, utilizando as seguintes fórmulas:
    a. Para homens: (72.7*h) - 58
    b. Para mulheres: (62.1*h) - 44.7 (h = altura)
    c. Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.
"""
def pesoIdealH(altura):
    pesoIdeal=(72.7*altura)-58
    return pesoIdeal

def pesoIdealM(altura):
    pesoIdeal=(62.1*altura)-44.7
    return pesoIdeal

def main():
    sexo=input("Qual seu sexo? ")
    altura=float(input("Qual sua altura? "))

    if sexo=="m":
        pesoIdeal=pesoIdealH(altura)
        print("O peso ideal para você homem é de ",pesoIdeal)
    else:
        pesoIdeal=pesoIdealM(altura)
        print("O peso ideal para você mulher é de ",pesoIdeal)






main()

