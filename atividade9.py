string=str(input('Informe uma string: '))
contador = 0
for char in string:
    if char.isalpha():
        contador+=1
print('A quantidade de letras:{} '.format(contador))


