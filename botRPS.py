import random
list = ["rock", "paper", "scissor"]


while True:
    def rps(bot, p2):
        if bot == p2:
            return "The game is tie!\n"
        elif p2 == "rock":
            if bot == "scissor":
                return "Player won\n"
            else:
                return "Bot won\n"
        elif p2 == "scissor":
            if bot == "paper":
                return "Player won\n"
            else:
                return "Bot won\n"
        elif p2 == "paper":
            if bot == "rock":
                return "Player won\n"
            else:
                return "Bot won\n"
        elif p2 != "rock" or p2 != "paper" or p2 != "scissor":
            return "Invalid Option!\n"

    bot = random.choice(list)
    p2 = input("PLAYER: rock, paper, scissor: ")

    print(f"Bot chose: {bot}")
    print(rps(bot, p2))

    reRun = input("Do you want to rerun[Y/N]: ")

    if reRun == "Y" or reRun == "y":
        continue
    else:
        break
