# crie um angoritimo que leia um numeor e mostre o seu dobro, triplo e Raiz quadrada.

N = int(input('Digite um numero '))
D= N*2
T= N*3
R= N**(1/2)
print('O dobro de {} vale {}.'.format (N,D))
print('O triplo de {} vale {}. /n A raiz quadrado de {} e igual a {:.2f}'.format (N,(N*3),N,pow (N,(1/2))))
