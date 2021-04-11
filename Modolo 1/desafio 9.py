# Faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario, com 5% de aumento

dias=int(input('Quantos dias Alugados? '))
km= float(input('Quants Km rodados?'))
pago=((dias *60)+km*0,15)
print('O Total a Pagar é de R${.2f}'.format(pago))
