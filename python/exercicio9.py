#!/usr/bin/env python3
# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. 
#     C = (F-32)/1.8
def main():
    F = float(input("Digite a temperatura em graus Farenheit "))
    C = F - 32
    C = C/1.8
    print("A temperatura ",F,"em graus Celsius é de",C)
main()    
	

