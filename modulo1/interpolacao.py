"""
  Interpolação básica de strings
  s -> string
  d e i -> int
  f -> float
  x e x -> Hexadecimal (ABCDEF0123456789)
       
"""
nome = 'Felipe'
preco = 1000.96897643
variavel = '%s , o preço è %.2f' %(nome, preco)
print(variavel)

print('O hexadecimal de %d é %04x ' %(15 , 15))