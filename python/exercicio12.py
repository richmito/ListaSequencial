#!/usr/bin/env python3
""" Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso
ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""
def main():
    altura = float(input("Insira sua altura "))
    alturaIdeal = (72.7*altura)-58
    print("Seu peso ideal é de ",alturaIdeal)
main()



