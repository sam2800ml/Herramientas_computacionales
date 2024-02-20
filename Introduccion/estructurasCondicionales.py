if __name__ == "__main__":
    def estaciones():
        mes = input("Ingresa el mes: ")
        mes.lower()
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

    def calculadora():
        valor_1 = int(input("Introduce el primer valor: "))
        valor_2 = int(input("Introduce el segundo valor: "))
        operacion = int(input("introduce el numero de la operacion que quieras realizar 1: suma, 2: resta, 3: multiplicacion, 4: division : "))

        if operacion == 1:
            resultado = valor_1 + valor_2
            print(f"El resultado de la operacion es de {resultado}")
        
        elif operacion == 2:
            resultado = valor_1 - valor_2
            print(f"El resultado de la operacion es de {resultado}")

        elif operacion ==3:
            resultado = valor_1 * valor_2
            print(f"El resultado de la operacion es de {resultado}")

        elif operacion == 4:
            resultado = valor_1 / valor_2
            print(f"El resultado de la operacion es de {resultado}")

        else:
            print("Esa operacion no se ha implementado todavia")

    #calculadora()
            
    class IMC():
        def __init__(self,estatura, peso, edad):
            self.estatura = estatura
            self.peso = peso
            self.edad = edad

        def indice(self):
            resultado = self.peso / self.estatura ** 2
            self.resultado = resultado
        
        def riesgo(self):
            self.indice()
            if self.edad >= 45:
                if self.resultado >= 22.0:
                    print(f"tu condicion de riesgo es alta tienes un IMC de {self.resultado}")
                else:
                    print(f"tu condicion de riesgo es medio tienes un IMC de {self.resultado}")
            else:
                if self.resultado >= 22.0:
                    print(f"tu condicion de riesgo es medio tienes un IMC de {self.resultado}")
                else:
                    print(f"tu condicion de riesgo es baja tienes un IMC de {self.resultado}")
        

    
    santiago=IMC(1.72,84,24)
    santiago.riesgo()



