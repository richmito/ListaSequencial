#!/usr/bin/env python3
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. 
def main():
    salario=float(input("Quanto você ganha por hora? "))
    horas=float(input("Quanto você trabalhou neste mês "))
    salarioFinal=salario*horas
    print("Seu salário será de R$",salarioFinal)
main()
