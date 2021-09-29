
'''This program gives all correct calculations except for 56+9, 45*3, 56/6 '''

while 1:
    print("what type of operation you want to perform?\n"
          "type + for addition\n"
          "type - for subtraction \n"
          "type * for multiplication\n"
          "type / for division\n")

    op = input("Enter a operator: ")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if op == "+":
        if num1 == 56 and num2 == 9:
            print("Answer is: 77")
        else:
            print("Answer is", num1 + num2)

    elif op == "*":
        if num1 == 45 and num2 == 3:
            print("Answer is: 555")
        else:
            print("Anser is:", num1 * num2)
    
    elif op == "/":
        if num1 == 56 and num2 == 6:
            print("Answer is: 4")
        else:
            print("Anser is:", num1 / num2)

    else:
        print("Answer is", num1 - num2)

    rerun = input('Do you want to rerun[Y/N]: ')
    if rerun == "Y" or rerun == "y":
        continue
    else:
        break
    