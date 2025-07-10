notaA = float(input("Digite sua primeira nota: "))
notaB = float(input("Digite sua segunda nota: "))

#calcular media
mediafinal = (notaA + notaB) /2

#verificação
if mediafinal >=7.0:
    print("A média: %.1f - Aprovado " % mediafinal)
else:
    print("A média: %.1f - Reprovado " % mediafinal)
