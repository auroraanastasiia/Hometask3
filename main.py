try:
 print("This program about two numbers ")
 c1 = int(input("Give me the first number :"))
 c2 = int(input("Give me the second number : "))
 if c1 == c2:
    print(c1, "equals ", c2)
 elif c1 > c2:
    print(c1, "bigger", c2)
 elif c1 < c2:
    print(c2, "bigger", c1)
finally:
    print("End of program ")