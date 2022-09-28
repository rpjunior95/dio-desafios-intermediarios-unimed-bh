letra = input()

num = 0
soma = 0

num = ord(letra)

for i in range(65,91):
    soma += 1
    if i == num:
        print(soma)
        break
