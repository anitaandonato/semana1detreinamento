km=int(input('Digite a distância em km: '))
if(km<=200):
  preço=1.5*km
else:
  preço=1.25*km
print('O preço da passagem é:{} '.format(preço))