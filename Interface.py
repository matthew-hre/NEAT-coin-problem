import Game

game = Game.Game()

while not game.test_end():
    input1 = input("Enter a number: ")
    input2 = input("Enter a number: ")
    input3 = input("Enter a number: ")
    new_output = f"{input1}{input2}{input3}"

    output = int(new_output, 2)

    if output == 0:
        score = game.switch(2)
    elif output == 1:
        score = game.switch(1)
    elif output == 2:
        score = game.switch(0)
    elif output == 3:
        score = game.promote(3)
    elif output == 4:
        score = game.promote(2)
    elif output == 5:
        score = game.promote(1)
    elif output == 6:
        score = game.promote(0)
    else:
        break

    print(game.game)

print("SCORE: ", game.score())
