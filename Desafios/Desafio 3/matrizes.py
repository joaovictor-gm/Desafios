print("Matrizes em Python: \n")

print("Exemplo 1:")
notas = [
    [8.5, 7.0, 9.0],
    [6.0, 8.5, 7.5]
]

print("Matriz de notas:")
for linha in notas:
    print(linha)
print()

print("Exemplo 2:")
print("Nota Aluno 1, Disciplina 2:", notas[0][1])

notas[1][2] = 9.0
print("Matriz atualizada:", notas)

media_aluno1 = sum(notas[0]) / 3
print("Média Aluno 1:", round(media_aluno1, 2))
print()

print("Exemplo 3:")
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

C_adicao = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        C_adicao[i][j] = A[i][j] + B[i][j]
print("Adição (A+B):", C_adicao)

D_subtracao = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        D_subtracao[i][j] = A[i][j] - B[i][j]
print("Subtração (A-B):", D_subtracao)
print()

try:
    import numpy as np
    print("Exemplo 4:")

    A_np = np.array(A)
    B_np = np.array(B)
    print("Adição NumPy:", A_np + B_np)

    matriz1 = np.array([[1, 2, 3], [4, 5, 6]])
    matriz2 = np.array([[7, 8], [9, 10], [11, 12]])
    print("Multiplicação:\n", np.dot(matriz1, matriz2))
    print()

    print("Exemplo 5:")
    original = np.array([[1, 2, 3], [4, 5, 6]])
    transposta = original.T
    print("Original:\n", original)
    print("Transposta:\n", transposta)
    print()

    print("Exemplo 6:")
    print("═" * 40)

    A_det = np.array([[3, 1], [2, 4]])
    det_A = np.linalg.det(A_det)
    print("Matriz A (2x2):\n", A_det)
    print("Determinante de A:", round(det_A, 6))

    B_det = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
    det_B = np.linalg.det(B_det)
    print("\nMatriz B (3x3):\n", B_det)
    print("Determinante de B:", det_B)

    if abs(det_A) < 1e-10:
        print("A é singular")
    else:
        print("A tem inversa")
    print()

    print("Exemplo 7:")
    print("═" * 40)

    print("Matriz A:\n", A_det)
    print("Det(A) =", round(det_A, 6))

    if abs(det_A) > 1e-10:
        inversa_A = np.linalg.inv(A_det)
        print("A inversa existe")
        print("Inversa de A:\n", np.round(inversa_A, 3))

        identidade = np.dot(A_det, inversa_A)
        print("Verificação A × A⁻¹ =\n", np.round(identidade, 3))
    else:
        print("Matriz não invertível")

    singular = np.array([[1, 2], [2, 4]])
    det_singular = np.linalg.det(singular)
    print(f"\nMatriz singular:\n{singular}")
    print("Det =", det_singular)
    print("NÃO tem inversa!")

except ImportError:
    print("NumPy não instalado!")
    print("No terminal: pip install numpy")
print("\n" + "="*60)