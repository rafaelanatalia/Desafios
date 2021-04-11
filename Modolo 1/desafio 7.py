# Faça um programa que leia a largura e a altura de uma parede em metros calcule sua area e a quantidade de tinta
# necessaria para pinta-la,
#sabendo que cada lata de tinta, pinta uma área de 2m².

#R$10*5/100

preço=float(input('Qual é o Preço do Produto?R$'))
novo = preço*5/100
nomo = preço-(5/100)
print('O produto que estava R${:.2f},na promoção com desconto de 5% vai custar R${}'.format(preço,nomo))