import time

OPTIONS = ['1','2','3','4','5','f','F']


print("Wellcome to open-source calculator!\n")

def calculator():
    while True:

        print("1) Sum\n"
              "2) Substract\n"
              "3) Mult.\n"
              "4) Divide\n"
              "F) Exit program\n")

        option = input("Please choose one of the options above: ")

        #EXIT FUNCTION
        if option == 'f' or option == 'F':
            print("\nClosing program...\n"
                  "Thank you for using our open-source calculator. Till next time ;)\n")
            break

        #WRONG OPTION
        if option not in OPTIONS:
            print("\nThere's no such option. Try again please.\n")
            time.sleep(1)
            continue

        number_1 = float(input("\nFirst number: "))
        number_2 = float(input("Second number: "))

        #SUM
        if option == '1':
            result = number_1 + number_2
            print("\nResult: {} + {} = {}\n".format(number_1, number_2, result))
            time.sleep(1)

        #MINUS
        elif option == '2':
            result = number_1 - number_2
            print("\nResult: {} - {} = {}\n".format(number_1, number_2, result))
            time.sleep(1)

        #MULT
        elif option == '3':
            result = number_1 * number_2
            print("\nResult: {} * {} = {}\n".format(number_1, number_2, result))
            time.sleep(1)

        #DIVIDE
        else:
            if number_2 == 0:
                print("\nNo number can be divided by zero.\n"
                      "Second number must be bigger than 0.\n"
                      "Try again please.\n")
                time.sleep(1)
                continue
            else:
                result = number_1 / number_2
                print("\nResult: {} / {} = {}\n".format(number_1, number_2, result))
                time.sleep(1)


calculator()