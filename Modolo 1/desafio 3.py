# Desemvolva um Programa que leia as duas notas de um Aluno, Calcule e mostre sua media

nome= input('Qual o nome do Aluno?')
pt = float (input('Qual a nota de Portugues: '))
mat = float (input('Qual a nota de Matematica: '))
his= float (input('Qual a nota de Historia: '))
m= (pt+mat+his)/3
print (' A media entre {} e {} é igual a {}'.format(pt,mat,his))
