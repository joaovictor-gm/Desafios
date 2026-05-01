""" Este código demonstra como acessar e modificar elementos de uma matriz,
além de calcular a média de um aluno. """

notas = [
    [8.5, 7.0, 9.0],
    [6.0, 8.5, 7.5]
]

print("Nota do Aluno 1 na disciplina 2:", notas[0][1])

notas[1][2] = 9.0   
print("Matriz atualizada:", notas)

media_aluno1 = (notas[0][0] + notas[0][1] + notas[0][2]) / 3
print("Média do Aluno 1:", media_aluno1)

soma = 0
for nota in notas[0]:
    soma += nota
media_aluno1_loop = soma / 3
print("Média do Aluno 1 (calculada com loop):", media_aluno1_loop)

soma_aluno2 = 0
for nota in notas[1]:
    soma_aluno2 += nota
media_aluno2 = soma_aluno2 / 3
print("Média do Aluno 2:", media_aluno2)