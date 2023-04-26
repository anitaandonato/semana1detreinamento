n1=int(input('Digite o valor de n1: '))
n2=int(input('Digite o valor de n2: '))
n3=int(input('Digite o valor de n3: '))


if (n1==n2 and n1==n3):
  print('Três iguais')
elif(n1==n2 or n1==n3 or n2==n3):
  print('Dois iguais')
else:
  print('Todos diferentes')