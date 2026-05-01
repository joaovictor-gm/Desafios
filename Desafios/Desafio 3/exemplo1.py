"""
Manual Prático: Introdução ao Uso de Matrizes em Python
Exemplo 1: Criando uma Matriz Simples

Este código demonstra como criar uma matriz 2x3 (2 linhas, 3 colunas) 
representando notas de alunos usando listas de listas em Python.
"""

notas = [
    [8.5, 7.0, 9.0],
    [6.0, 8.5, 7.5]
]

print("Matriz de notas:")
for linha in notas:
    print(linha)

print("\nAcesso a elementos específicos:")
print("Nota do Aluno 1 na disciplina 1:", notas[0][0])
print("Nota do Aluno 1 na disciplina 2:", notas[0][1])
print("Nota do Aluno 1 na disciplina 3:", notas[0][2])
print("Nota do Aluno 2 na disciplina 1:", notas[1][0])
print("Nota do Aluno 2 na disciplina 2:", notas[1][1])
print("Nota do Aluno 2 na disciplina 3:", notas[1][2])