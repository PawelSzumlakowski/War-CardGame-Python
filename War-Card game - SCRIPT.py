from WarCardGame import *
# import WarCardGame print(WarCardGame.cardList[0].name)
import time

# Card.shuffle(cardList)


total_quantity = 1

while total_quantity:
    total_quantity = sum(card.quantity for card in cardList)
    for player in range(len(playersList)):
        playersList[player].drawCard()


for k in range(len(playersList)):
    print("Player {:5}, has {} cards. {}".format(
        playersList[k].name, len(playersList[k].selectedCards), "#" * len(playersList[k].selectedCards)))

gameOn = True

roundNum = 1

while gameOn:

    print("Round", roundNum)

    roundNum += 1

    stack = []

    if len(playersList[0].selectedCards) == 0 or len(playersList[1].selectedCards) == 0:
        print("\nOne player has no cards")
        gameOn = False
        if len(playersList[0].selectedCards) == 0:
            print("\nPlayer {} won this game \n\n".format(playersList[1].name))
        elif len(playersList[1].selectedCards) == 0:
            print("\nPlayer {} won this game \n\n".format(playersList[0].name))
        break

    else:

        PawelsCard = playersList[0].selectedCards.pop(0)
        ElasCard = playersList[1].selectedCards.pop(0)

        print("Player's name {:5}, card: {:5}, card's power {:2}".format(
            playersList[0].name, PawelsCard.name, PawelsCard.power))
        print("Player's name {:5}, card: {:5}, card's power {:2}".format(
            playersList[1].name, ElasCard.name, ElasCard.power))

        if PawelsCard.power == ElasCard.power:

            print("\n\t*****WAR*****\n")

            while PawelsCard.power == ElasCard.power and len(playersList[0].selectedCards) > 1 and len(playersList[1].selectedCards) > 1:

                stack.append(PawelsCard)
                stack.append(ElasCard)

                PawelsSecondCard = playersList[0].selectedCards.pop(0)
                ElasSecondCard = playersList[1].selectedCards.pop(0)
                stack.append(PawelsSecondCard)
                stack.append(ElasSecondCard)

                print("Wystarczająca ilość kart")

                if len(playersList[0].selectedCards) < 1:

                    playersList[1].selectedCards += stack

                    playersList[1].selectedCards.append(
                        playersList[0].selectedCards.pop(0))
                    playersList[1].selectedCards.append(
                        playersList[0].selectedCards.pop(0))

                    print(" Line 76 \nPlayer {} won game\n".format(
                        playersList[1].name.upper()))

                    break

                elif len(playersList[1].selectedCards) < 1:

                    playersList[0].selectedCards += stack
                    playersList[0].selectedCards.append(
                        playersList[1].selectedCards.pop(0))
                    playersList[0].selectedCards.append(
                        playersList[1].selectedCards.pop(0))

                    print(" Line 89 \nPlayer {} won game\n".format(
                        playersList[0].name.upper()))
                    break

                else:
                    PawelsCard = playersList[0].selectedCards.pop(0)
                    ElasCard = playersList[1].selectedCards.pop(0)

            else:
                print("Line 98")
                if PawelsCard.power > ElasCard.power:

                    playersList[0].selectedCards += stack
                    playersList[0].selectedCards.append(PawelsCard)
                    playersList[0].selectedCards.append(ElasCard)

                    print("Player {} won this battle\n".format(
                        playersList[0].name.upper()))

                elif ElasCard.power > PawelsCard.power:

                    playersList[1].selectedCards += stack
                    playersList[1].selectedCards.append(PawelsCard)
                    playersList[1].selectedCards.append(ElasCard)

                    print("Player {} won this battle\n".format(
                        playersList[1].name.upper()))

                elif ElasCard.power == PawelsCard.power:
                    playersList[0].selectedCards.append(PawelsCard)
                    playersList[1].selectedCards.append(ElasCard)
                    print("Line 122")
                    # conf = input("Please confirmate the error form 121 line".upper())
                else:
                    # print("Program run into a problem in while loop, line 115")
                    # conf = input("Please confirmate the error form 114 line")
                    continue

                stack.clear()

        elif PawelsCard.power > ElasCard.power:

            print("Pawel's card has higher power. Hidding")
            playersList[0].selectedCards.append(ElasCard)
            playersList[0].selectedCards.append(PawelsCard)

        elif PawelsCard.power < ElasCard.power:

            print("Ela's card has higher power. Hidding")
            playersList[1].selectedCards.append(PawelsCard)
            playersList[1].selectedCards.append(ElasCard)

        for k in range(len(playersList)):
            print("Player {:5}, has {} cards. {}".format(
                playersList[k].name, len(playersList[k].selectedCards), "#" * len(playersList[k].selectedCards)))

        time.sleep(0)


entry = input("Enter key to exit")
