def mult(num):
   resultado = float(num) * float(multiplicador)
   return resultado


####################
print("Calculadora de multiplicação \n")
####################


while True:
   numero = input("Número a ser multiplicado: ")
   if numero.isdigit():
      multiplicador = input("Vezes: ")


      if multiplicador.isdigit():
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
