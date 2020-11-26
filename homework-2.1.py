# coding: latin-1
# Fazer um programa que pergunte a temperatura em Celsius e converte para Fahrenheit

print("Insira a temperatura em Celsius:")
n1 = int(input())
n2 = n1 * 1.8 + 32

print(f"A temperatura é °F {round(n2,2)}")