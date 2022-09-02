# ----------Manipulando Texto-----------

frase = '   Curso em Vídeo Python'
# print(frase[:15:2])

print(frase.count(''))
print(frase.upper().count('O'))

print(len(frase.strip()))#remove espaço
print(len(frase))

#print(frase.replace('Python', 'TrocarPalavra'))
frase=frase.replace('Python','Android') 
print(frase)

print('Curso' in frase)
print(frase.find('Curso'))
print(frase.lower().find('vídeo'))
print(frase.split())
dividido = frase.split()
print(dividido[2][3])
# print("""Lorem jndkjfjk kljsdfnkjsnelkfjd ljasnfkjnafsnkjdnf ljnasfçkjnçkafjbckljf 
# kABSÇFJKNFÇLJADNFÇOJLanfkbrv  klj.ndflkvb lkwdjasbcx kljsdnfçkjneçwkd çlwe.njfd cj nd jnef
# çwfdjkncçkjbnfçkdjgn vnlkjhij lkjhhbjn  uigkjghfhjbujiçjb uohuigiuhln jçkjgdgbhb """)
