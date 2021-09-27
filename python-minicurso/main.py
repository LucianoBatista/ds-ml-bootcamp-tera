fn = lambda x: x ** 2

numbers = [1, 5, 6, 6, 8, 2, 0, 5, 15]

# lambda <params> : <operation>
list_sorted = sorted(numbers, key=lambda x: x * 10 if (x % 2 == 1) else x)

m3 = lambda x: x * 3
print(m3(5))

# temas
# Investimento - Finanças (chatbot)
# Educação - NLP
# Impregabilidade 
# Finanças - Impacto da pandemia na análise de crédito

nomes = dicionario.get("Nomes")
indexes = [i for _, i in enumerate(nomes)]

for nome in nomes:
    index = dicionario.get("Nomes")