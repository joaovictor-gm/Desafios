""" Este código demonstra como realizar operações de adição e subtração de matrizes
usando listas nativas e NumPy. """

print("=== Usando listas nativas ===\n")

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

C_adicao = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2): 
        C_adicao[i][j] = A[i][j] + B[i][j]

print("Matriz A:", A)
print("Matriz B:", B)
print("Adição das matrizes (A + B):", C_adicao)

D_subtracao = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        D_subtracao[i][j] = A[i][j] - B[i][j]

print("Subtração das matrizes (A - B):", D_subtracao)

print("\n=== Usando NumPy ===\n")

import numpy as np

A_np = np.array([[1, 2], [3, 4]])
B_np = np.array([[5, 6], [7, 8]])

C_adicao_np = A_np + B_np
D_subtracao_np = A_np - B_np

print("Adição com NumPy:")
print(C_adicao_np)

print("\nSubtração com NumPy (A - B):")
print(D_subtracao_np)

print("\n=== Exemplo prático: Vendas semanais ===\n")


vendas_semana1 = np.array([[100, 150, 200],
                          [80, 120, 90]]) 

vendas_semana2 = np.array([[120, 130, 180],
                            [95, 110, 100]])

total_vendas = vendas_semana1 + vendas_semana2

print("Vendas Semana 1:")
print(vendas_semana1)
print("\nVendas Semana 2:")
print(vendas_semana2)
print("\nTotal de vendas (Semana 1 + Semana 2):")
print(total_vendas)

diferenca = vendas_semana2 - vendas_semana1
print("\nDiferença (Semana 2 - Semana 1):")
print(diferenca)