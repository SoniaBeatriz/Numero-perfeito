import math

def eperfeito(n):
    soma = 0
    for i in range(1, math.ceil(n/2)+1):
        if n % i == 0:
            soma += i
    if soma == n:
        return True
    return False

while True:
    try:
        num1 = int(input('insira o numero inicial: '))
        num2 = int(input('insira o numero final: '))
    except ValueError:
        print('insira um número válido')
        continue
    if num1 < 2:
        print('valor de entrada inválido!')
        continue
    elif num2 > 1000:
        print('valor de entrada inválido!')
        continue
    break

perfeitos = []
for num in range(num1, num2+1):
    if eperfeito(num):
        perfeitos.append(num)
if len(perfeitos) == 0:
    print('não há números perfeitos no intervalo escolhido')
else:
    print(perfeitos)        