# teste dos tipos primitivos
n = input('digite algo: ')
print('o tipo primitivo é:' , type(n))
print('só tem espaços? = ' , n.isspace())
print('é númerico? = ' , n.isnumeric())
print('é uma letra? = ' , n.isalpha())
print('é alfanúmerico? = ' , n.isalnum())
print('está totalmente maiusculo? = ' , n.isupper())
print('está totalmente minúsculo? = ' , n.islower())
print('está capitalizado?' , n.istitle())