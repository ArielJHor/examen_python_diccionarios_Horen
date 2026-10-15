tienda = {
    "Terror": ["Five Night At Marchenas", "Gorila Aplastar Ciudad Abuelita Miedo"],
    "ciencia ficción": ["The Last of Jeffrey"],
    "accion": ["Sobrevive en la ETec"],
}
biblioteca = {}

while True:
    print("- - - - - - - - - - - - - -")
    print("|      ETec Station      |")
    print("|                        |")
    print("- - - - - - - - - - - - - -")
    print("1. Tienda")
    print("2. Jugar a un juego")
    print("3. Salir")
    op = input("Opcion: ")
    if op == "1":
        print("1. comprar")
        print("2. Ingresar")
        op = input("Opsion: ")
        if op == "1":
            g = input("que genero: ")
            for i, juego in (tienda[g]): 
                  print("")
