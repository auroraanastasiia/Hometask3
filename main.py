try:
 print("This program about two actions with two numbers ")
 k1 = int(input("Give me the first number :"))
 k2 = int(input("Give me the second number :"))
 math_action = input("Enter math action:")
 sum1  = k1+k2
 minus = k1 - k2
 multip1 = k1*k2
 division = k1/k2
 match math_action:
    case '+':
        print (sum1)
    case '-':
        print(minus)
    case '*':
        print(multip1)
    case '/':
        print(division)
    case _:
        print("It is not right for program")
except ZeroDivisionError as error:
     print(f"ZeroDivisionError occurred: {error}")
except ValueError as error:
         print("Enter only integer numbers please!")
         print(f"ValueError: {error}")
finally:
 print("End of calculation")