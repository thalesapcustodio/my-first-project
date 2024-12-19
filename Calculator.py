####################


print("Calculadora de números")


####################
def mult(numero):
   resultado = float(numero) * float(multiplicador)
   return resultado


print("Calculdadora de multiplicação")
print("")


while True:
   numero = input("Número a ser multiplicado: ")
   if numero.isdigit() == True:
      multiplicador = input("Vezes: ")


      if multiplicador.isdigit() == True:
         print("Resultado: ",(mult(numero)))
         print("")


      elif multiplicador == "exit":
         print("Programa fechado pelo usuário")
         break


      else:
         print(numero, "Não é um número, tente novamente.")
         print("")


   elif numero == "exit":
      print("Programa fechado pelo usuário")
      break


   else:
      print(numero, "Não é um número, tente novamente.")
      print("")
