
# forma diferente de usa o print em operações aritimeticas:

print('\n')

n1 = int(input('digite um valores: '))

n2 = int(input('digite outro valor: '))

s = n1 + n2 
f = n1 - n2 
g = n1 * n2
d = n1 / n2 
di = n1 // n2
e = n1 ** n2

print('\n')

print('A soma é {}, a multiplicação é {}, a divisão é {:.2f}'.format(s,g,d), end=' ' )
print(',a divisão inteira é {}, a potencia é {}, e a subtração é {}'.format(di,e,f))

print('\n')