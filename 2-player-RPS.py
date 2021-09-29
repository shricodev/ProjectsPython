def rps(p1, p2):
    if p1 == p2:
        return "The game is tie!"
    elif p1 == "scissor":
        if p2 == "rock":
            return "Player2 won"
        else:
            return "Player1 won"
    elif p1 == "paper":
        if p2 == "scissor":
            return "Player2 won"
        else:
            return "Player1 won"
    elif p1 == "rock":
        if p2 == "paper":
            return "Player2 won"
        else:
            return "Player1 won"
    else:
        return "Invalid Option!"


p1 = input("PLAYER1: rock, paper, scissor: ")
p2 = input("PLAYER2: rock, paper, scissor: ")


print(rps(p1, p2))