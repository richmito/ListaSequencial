#!/usr/bin/env python3
# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#
# a) o produto do dobro do primeiro com metade do segundo .
# b) a soma do triplo do primeiro com o terceiro.
# c) o terceiro elevado ao cubo. 

def main():
    int1=int(input("Insira o primeiro número inteiro "))
    int2=int(input("Insira o segundo número inteiro "))
    float1=float(input("Insira o número real "))
    resultado1=(2*int1)*(int2/2)
    resultado2=(3*int1)+float1
    resultado3=float1*float1*float1

    print("O produto do dobro do primeiro com metade do segundo é: ",resultado1)
    print("A soma do triplo do primeiro com o terceiro é: ",resultado2)
    print("O terceiro elevado ao cubo é: ",resultado3)
    input("")
main()
	

