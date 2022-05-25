class calculadora():
    valor1= 0
    valor2= 0


    def __init__(self,valor1,valor2):
        self.valor1= float(valor1)
        self.valor2= float(valor2)

    def sumar(self):
        suma = self.valor1+self.valor2
        print("La suma es: ", suma)
    
    def restar(self):
        resta = self.valor1-self.valor2
        print("La resta es: ", resta)

    def multiplicar(self):
        multiplicacion = self.valor1*self.valor2
        print("La multiplicación es: ", multiplicacion)

    def dividir(self):
        divicion = self.valor1/self.valor2
        print("el resultado de la divición es: ", divicion)

valor1 = input("Ingrese un número: ")
valor2 = input("Ingrese un número: ")

calculadora = calculadora(valor1,valor2)

