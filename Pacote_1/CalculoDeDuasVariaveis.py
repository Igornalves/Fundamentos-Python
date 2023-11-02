
# sistema simples de calculo de duas variaveis em python:

print('\n')

print('                      Bem vindo ao sistema de calculo de duas variaveis')

print ('\n')

n1 = int(input('                              digite um número: '))
n2 = int(input('                              digite outro número: '))

soma = n1 + n2
subtra = n1 - n2
multi = n1 * n2
divi = n1 / n2

print('\n')

# print('                          a soma de',n1,'+',n2,'é igual a =', soma)
print('                           a soma de {} + {} é igual a = {}'.format(n1, n2, soma))

print('\n')

# print('                          a subtração de',n1,'-',n2,'é igual a =',subtra)
print('                           a subtração dos números {} - {} é igual a = {}'.format(n1, n2, subtra))

print('\n')

# print('                          a multiplicação dos números',n1,'x',n2,'é igual a =',multi)
print('                           a multiplicação do números {} x {} é igual a = {}'.format(n1, n2, multi))

print('\n')

# print('                           a divisão dos números',n1,'/',n2,'é igual a =',divi)
print('                           a divisão dos números {} / {} é igual a = {}'.format(n1, n2, divi))

print('\n')
