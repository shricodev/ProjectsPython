import random

list = ["S", "W", "G"]
play = 10
p_point = 0
b_point = 0
# i = 1

diction = {
    "S" : "Snake",
    "W" : "Water",
    "G" : "Gun" 
}

try:
    while play != 0:
        def swg(bot, user):
            global p_point
            global b_point

            if user == bot:
                return "Tie!\n"
            elif user == "S":
                if bot == "G":
                    b_point += 1
                    return "Bot won\n"
                else:
                    p_point += 1
                    return "Player won\n"
            elif user == "W":
                if bot == "S":
                    b_point += 1
                    return "Bot won\n"
                else:
                    p_point += 1
                    return "Player won\n"
            elif user == "G":
                if bot == "W":
                    b_point += 1
                    return "Bot won\n"
                else:
                    p_point += 1
                    return "Player won\n"

        bot = random.choice(list)
        user = input("Enter S for snake, W for water, G for gun: ")
        # print('Bot chose', bot)
        for i in range (1):
            print("Bot chose", diction[bot])
        print(swg(bot, user))
        play -= 1

    print("---------------")
    print("Player Points: ", p_point)
    print("Bot Points: ", b_point)
    print("---------------")


    if b_point > p_point:
        print('Bot won by', b_point - p_point, "points")
    elif b_point == p_point:
        print("The game is tie!")
    else:
        print("Player won by", p_point - b_point, "points")

except Exception as e:
    print("System Failure!")
