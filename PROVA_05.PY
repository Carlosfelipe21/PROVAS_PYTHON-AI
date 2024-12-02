# Crie uma função chamada maior_numero que receberá três números como argumentos. 
# Esta função deve comparar os três números e identificar qual deles é o maior. 
# Para isso, utilize uma estrutura de controle que verifique qual número é maior que os outros dois. 
# A função deve então retornar o maior número encontrado.

def maior_numero(numero_01, numero_02, numero_03):
    if numero_01 > numero_02 and numero_01 > numero_03:
        return f"Maior numero encontrado: {numero_01}"
    elif numero_02 > numero_01 and numero_02 > numero_03:
        return f"Maior numero encontrado: {numero_02}"
    else:
        f"Maior numero encontrado: {numero_03}"

resultado = maior_numero(numero_01 = 15, numero_02 = 26, numero_03 = 12)
print(resultado)
 

