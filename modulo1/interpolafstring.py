"""
Formatação básica de strings
s - strings
d - int
f - float
.<número de digitos>f
x ou X - Hexadecimal
(Caractere) (><^)(quantidade)
> - Esquerda
< - direita
^- Centro
Sinal - + ou -
ex.: 0>-100,.1f
conversion flags - !r !s !a
    
"""
nome = 'Felipe'
print(f'{nome: >12}.')
print(f'{nome: ^12}.')
print(f'{nome: <12}.')

