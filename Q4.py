'''4. Crie duas funções:

○ A primeira função receberá dois parâmetros e retornará como resultado uma
concatenação de texto colocando uma vírgula entre os dois parâmetros ao
uní-los.

○ A segunda função não receberá parâmetros; será feito a leitura de duas
entradas que o usuário digitar; irá chamar a primeira função passando como
argumento os dois textos lidos; por fim esta segunda função irá imprimir para
o usuário informando qual foi o resultado que se obteve na chamada à
primeira função.
○ Exemplo da primeira entrada: “Olá”. Exemplo da segunda entrada: “Mundo”.
Exemplo da saída do sistema: “Olá,Mundo”.'''

def concat(ent1, ent2):
    return ent1+','+ent2 
           #f'{ent1},{ent2}'

def print_saída():
    ent1 = input('Digite a primeira entrada: ')
    ent2 = input('Digite a segunda entrada: ')

    print(concat(ent1, ent2))


print_saída()