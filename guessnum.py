import random

n = random.randint(0, 21)
guess_left = 9

print("The range of guessing number is between 0-20")

while True:

    print("Guesses left is: ", guess_left)
    user = int(input("Enter your guess: "))

    if user == n and guess_left >= 1:
        print("Yippee! You guessed it correctly")
        print(f"You took {9-guess_left} no of guesses to finish")
        print("Guesses left is: ", guess_left)

    elif user < n and guess_left >=1:
        print("Incorrect guess! go little higher")
        guess_left -= 1
        print("Guesses left is", guess_left)

    elif user > n and guess_left >= 1:
        print("Incorrect guess! go little lower")
        guess_left -= 1
        print("Guesses left is", guess_left)

    # elif user > n and guess_left >= 1:
    #     print("Sutta marke baitha hai kya?")
    #     guess_left -= 1
    #     print("Guesses left is", guess_left)

    if guess_left >= 1:
        rerun = input("Do you wanna rerun[Y/N]: ")
 
    if rerun == "Y" or rerun == "y":
        if guess_left >= 1:
            continue
        else:
            print("Game Over!")
            break

    elif rerun == "N" or rerun == "n":
        break 



'''This is also a great code to do the same thing but without random module'''

# n=18
# number_of_guesses=1
# print("Number of guesses is limited to only 9 times: ")
# while (number_of_guesses<=9):
#     guess_number = int(input("Guess the number :\n"))
#     if guess_number<18:
#         print("you enter less number please input greater number.\n")
#     elif guess_number>18:
#         print("you enter greater number please input smaller number.\n ")
#     else:
#         print("you won\n")
#         print(number_of_guesses,"no.of guesses he took to finish.")
#         break
#     print(9-number_of_guesses,"no. of guesses left")
#     number_of_guesses = number_of_guesses + 1

# if(number_of_guesses>9):
#     print("Game Over")
