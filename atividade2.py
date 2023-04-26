n1=int(input('Digite o valor de n1: '))
n2=int(input('Digite o valor de n2: '))
n3=int(input('Digite o valor de n3: '))
n4=int(input('Digite o valor de n4: '))
n5=int(input('Digite o valor de n5: '))
numeromaior=0
if(n1>n2):
  numeromaior=n1
else:
  numeromaior=n2
if (n3>numeromaior):
  numeromaior=n3
if (n4>numeromaior):
  numeromaior=n4
if (n5>numeromaior):
  numeromaior=n5 
print('O maior número é: {}'.format(numeromaior))