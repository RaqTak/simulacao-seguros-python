simulacoes = 100
resultados = []

for j in range(simulacoes):
    total_sinistros = 0
    custo_total = 0

    for i in range(num_clientes):
        if random.random() < prob_acidente:
            total_sinistros += 1
            custo_total += random.randint(3000, 7000)

    resultados.append(custo_total)

media = sum(resultados) / len(resultados)

print("Custo médio após várias simulações:", media)
