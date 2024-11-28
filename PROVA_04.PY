# Crie uma função chamada media que receberá três números como argumentos. 
# Esta função deve calcular a média aritmética desses três números. 
# Para fazer isso, some os três números e, em seguida, divida o resultado por três. 
# Por fim, a função deve retornar o valor da média aritmética calculada



def media(numero_1, numero_2, numero_3):
    return (numero_1 + numero_2 + numero_3) /3

media_aritmetica = f"A media aritmetica é {media(numero_1=10, numero_2=20, numero_3=30):.2f}"
print(media_aritmetica)
