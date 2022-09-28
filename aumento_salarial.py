salario = int(input())

if (0 <= salario <= 600):
    percentual = 17
    reajuste = salario * (percentual / 100)
    salario += reajuste
elif (600.01 <= salario <= 900):
    percentual = 13
    reajuste = salario * (percentual / 100)
    salario += reajuste
elif (900.01 <= salario <= 1500):
    percentual = 12
    reajuste = salario * (percentual / 100)
    salario += reajuste
elif (1500.01 <= salario <= 2000):
    percentual = 10
    reajuste = salario * (percentual / 100)
    salario += reajuste
else:
    percentual = 5
    reajuste = salario * (percentual / 100)
    salario += reajuste

print(f'Novo salario: {salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {percentual} %')