def main():
edad=int(input("Ingresa tu edad: "))
id=input("¿Tienes identificación oficial? (s/n): ")
if edad<=0:
    print("Respuesta incorrecta")
elif id!="s" or "n":
    print("Respuesta incorrecta")
elif edad<18 and id=="n":
    print("No cumples requisitos")
elif edad>18 and id=="n":
    print("No cumples requisitos")
elif edad<18 and id=="y":
    print("No cumples requisitos")
elif edad>=18 and id=="y":
    print("Trámite de licencia concedido")
    pass


if __name__ == '__main__':
    main()
