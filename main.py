try:
 print("Hello this program about days of the week!")
 n1 = int(input("Give me numbers from 1 to 7 :"))
 if n1 == 0:
    print("Please enter non-zero number!")
 elif n1 > 7:
    print("This number is not for program")
 elif n1 == 1:
    print("Monday")
 elif n1 == 2:
    print("Tuesday")
 elif n1 == 3:
    print("Wednesday")
 elif n1 == 4:
    print("Thursday")
 elif n1 == 5:
    print("Friday")
 elif n1 == 6:
    print("Saturday")
 elif n1 == 7:
    print("Sunday")

except ValueError as error:
    print("Enter only integer numbers please!")

finally: print("End of the program")
