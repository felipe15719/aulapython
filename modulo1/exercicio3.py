primeiro = input("Digite um valor: ")
segundo = input("Digite outro valor: ")


if primeiro > segundo:
    print(f"o primeiro valor é {primeiro}"
          f" maior que o segundo {segundo}")
elif segundo > primeiro :
    print(f"o segundo valor é {segundo}"
          f" maior que o primeiro valor {primeiro}")
else:
    print("os valore são iguais")