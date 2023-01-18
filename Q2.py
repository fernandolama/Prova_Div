num = int(input('Digite um número, por favor: '))
resto = num % 2

if num < 10:
    print("O número é menor do que 10.")

if resto == 0:
    print("O número é par.") 

if num >= 8 and num <= 16:
    print("O número está entre 8 e 16.")

if num == 51 or num == 80:
    print("O número é 51 ou 80.")