if __name__ == "__main__":

    while True:
        palabra = input("Introduce una palabra para verificar si es palindromo: ")
        palindromo = palabra[::-1]
        
        if palabra == palindromo:
            print(f"Felicitaciones {palabra} es igual a {palindromo}")
            break
        else:
            print(f"La palabra {palabra} no es palindromo ya que {palindromo} no son iguales")

    def ciclo():
        print("Bienvenido a la suma de numeros dentro del rango el cual das")
        numero_1 = int(input("Introduce el primer numero: "))
        numero_2 = int(input("Introduce el segundo numero numero: "))
        numeros = []
        if numero_1 > numero_2:
            print("No se puede realizar ya que el primer numero es mayor al segundo")
        else:
            for i in range(numero_1, numero_2 -1 ):
                numeros.append(i+1)
            print(sum(numeros))

    #ciclo()