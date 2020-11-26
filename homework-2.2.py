# coding: latin-1
# Calculadora para saber a rentabilidade de uma venda de ações

print("Nome da ação:")
nome = input()

print("Quantidade de ações vendidas")
qtd = int(input())

print("Preço de compra da ação:")
pc = float(input())
tc = pc * qtd  # preço de compra x quantidade comprada = 780,00

print("Preço de venda da ação")
pv = float(input())
tv = pv * qtd  # preço de venda x quantidade comprada = 1000,00

prof = round(float(tv - tc), 0)
rent = round(prof / tc * 100, 2) # lucro / compra
print(f"A ação {nome} foi vendida com uma rentabilidade real de {rent}%")
print(f"Seu lucro com {nome} foi de R$ {prof}")