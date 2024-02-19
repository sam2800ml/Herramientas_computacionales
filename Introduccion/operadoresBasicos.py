if __name__ == "__main__":
    def sayhi():
        name = str(input("Introduce tu nombre por favor: "))
        print(f"hola {name}, como has estado?")    


    def horas():
        segundos = float(input("Introduce los segundos, y te los convertire: "))

        minutos = segundos / 60.0
        horas = segundos / 3600
        dias = segundos / 86400


        print(str(minutos).zfill(2))

    #horas()

    def enteros():
        numero = int(input("Introduce un numero: "))

        if numero > 0:
            for i in range(1,numero + 1):
                sum = ((i)*(i+1))/2
                print("suma",sum,i)

    #enteros()
                
    
