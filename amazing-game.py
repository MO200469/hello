# Purpose: A two-player game that lets you choose a number from 1 to 10 and adds it to the sum.
#         The first player that gets to 100 wins and if the sum is more than 100 the game ends in draw


def main():
    # Initializing the sum, Welcome screen, and displaying the rules and the sum
    sum = 0
    print("Welcome to 100 game")
    print("First player to get the sum to 100 wins!")
    print("But be careful! if a player gets the sum over 100 the game ends in a draw!")
    print("Sum =", sum)
    print("Please choose an integer from 1 to 10")

    # Updating the sum and displaying it
    while True:
        sum += get_int(1)
        print("Sum =", sum)
        win(1, sum)
        sum += get_int(2)
        print("Sum =", sum)
        win(2, sum)


def get_int(x):
    # Getting input of an integer from the user from 1 to 10 and rejecting anything else
    while True:
        try:
            number = int(input("Player {}: ".format(x)))
            if (1 <= number <= 10):
                return number
            else:
                print("Please choose an integer from 1 to 10")
        except ValueError:
            print("The input is not an integer")
            print("Please choose an integer from 1 to 10")


def win(y, sum):
    # if the sum is 100 display the winner and end game
    if sum == 100:
        print(f"Player {y} has won")
        exit()
    # if the sum is more than 100 display that the game ended in a draw and end game
    if sum > 100:
        print("The game ended in a draw")
        exit()


main()
