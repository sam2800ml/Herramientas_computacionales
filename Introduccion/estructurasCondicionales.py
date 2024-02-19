if __name__ == "__main__":
    def estaciones():
        mes = input("Ingresa el mes: ")
        numero = int(input("Ingresa el dia: "))

        if mes == "enero" or "febrero":
            print(f"Tu estacion actual es de Invierno")
        elif mes == "marzo":
            if numero < 20:
                print(f"Tu estacion actual es de Invierno")
            else:
                print(f"Tu estacion actual es de Primavera")
        elif mes == "abril" or "mayo":
            print(f"Tu estacion actual es de Primavera")
        elif mes == "junio":
            if numero < 21:
                print(f"Tu estacion actual es de Primavera")
            else:
                print(f"Tu estacion actual es de Verano")
        elif mes == "julio" or "agosto":
            print(f"Tu estacion actual es de Verano")
        elif mes == "septiembre":
            if numero < 22:
                print(f"Tu estacion actual es de Verano")
            else:
                print(f"Tu estacion actual es de Otoño")
        elif mes == "octubre" or "noviembre":
            print(f"Tu estacion actual es de Otoño")
        elif mes == "diciembre":
            if numero < 21:
                print(f"Tu estacion actual es de Otoño")
            else:
                print(f"Tu estacion actual es de Invierno")

    estaciones()





