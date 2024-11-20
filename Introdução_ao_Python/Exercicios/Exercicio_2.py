"""
* Substituindo caractere repetido:
-> Escreva um programa Python para obter uma string de uma determinada string 
em que todas as ocorrências de seu primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere
Ex: fifa 24 → fi$a 24
"""

name = "Fifa"
char = name[0].lower() # Pegamos a primeira letra e deixamos minuscula 
new_name = name.replace(char, "$") # Alteramos todas as letras iguais a char para $
new_name =  char + new_name[1:] # Concatenamos as strings, mantendo a primeira letra inalterada
print(new_name) 

"""
* Substituindo caractere repetido
-> Escreva um programa Python para obter uma única string de duas strings fornecidas, separadas por um espaço e 
troque os dois primeiros caracteres de cada string.
Ex: abc xyz → xyc abz
"""

name2 = "abc xyz"
char1 = name2[0].lower() + name2[1].lower() # Pegamos o primeiro e segundo caracterer do name2
char2 = name2[4].lower() + name2[5].lower() # Pegamos o quarto e quinto caracterer do name2
aux1 = name2[:3] # Separamos a primeira parte da string, índice final -1
aux2 = name2[4:7] # Separamos a segunda parte da string, índice final -1
new_name_aux1 = aux1.replace(char1, char2) # Alteramos as duas primeiras letras da string pela string presente em char2
new_name_aux2 = aux2.replace(char2, char1) # Alteramos as duas primeiras letras da string pela string presente em char1
new_name2 = new_name_aux1 + " " + new_name_aux2 # Concatenamos a string
print(new_name2)