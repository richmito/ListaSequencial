#!/usr/bin/env python3
"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento
diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo
excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e
verifique se há excesso. Se houver, gravar na variável excesso e na variável multa o valor da multa
que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO.
"""
def verificarExcedente(peso):
    if peso>50:
        excedente=peso-50
    else:
        excedente=0
    return excedente

def calcularMulta(excedente):
    multa=excedente*4
    return multa


def main():
    peso=float(input("Seu João, qual o peso do peixe? "))
    excedente=verificarExcedente(peso)
    multa=calcularMulta(excedente)
    print("Seu João, hoje você pagará multa no valor de R$",multa)
    



main()

