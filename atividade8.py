palavra1='treinamento'
palavra2='hoje'
palavra3='de'
palavra4='backend'
frase=palavra1+" "+palavra2+" "+palavra3+" "+palavra4
print(frase)
palavras=str(input('Informe a palavra que deseja substituir totalmente maiúscula ou totalmente minúscula: '))
palavrasubstituta=str(input('Informe a palavra substituta: '))
if(palavras=="treinamento" or palavras=="TREINAMENTO"):
    frase=palavrasubstituta+" "+palavra2+" "+palavra3+" "+palavra4
elif(palavras=="hoje" or palavras=="HOJE"):
    frase=palavra1+" "+palavrasubstituta+" "+palavra3+" "+palavra4
elif(palavras=="de" or palavras=="DE"):
    frase=palavra1+" "+palavra2+" "+palavrasubstituta+" "+palavra4
elif(palavras=="backend" or palavras=="BACKEND"):
    frase=palavra1+" "+palavra2+" "+palavra3+" "+palavrasubstituta
else:
    print('Inválido! Tente novamente!')
print(frase)