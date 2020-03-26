# Jackson J.
# 3.23.2020
# This is the Driver file for the Stockholders Portfolio
from Queue import Queue
from Stack import Stack
# If the user chooses FIFO then this will be used
MyQueueShare = Queue()
MyQost = Queue()

# If the user chooses LIFO then this will be used
MyStackShare = Stack()
MyCoSt = Stack()

# The Shares and the Profit will not need to be separate variables for each method.
# This will just be added to accordingly
Shares = 0
Profit = 0

# This will how the type of report method
choice = "Hello World"

input('PRESS ENTER')
input("\nWelcome to the Stockholders Portfolio program"
      "\nIn just a moment you will prompted to type which way you wish to report profits:"
      "\nL for LIFO"
      "\nF for FIFO"
      "\nBe weary of the fact that which ever choice you choose use will stick with you."
      "\n\nPRESS ENTER")

# Ask the user how they will report their shares FIFO or LIFO (One time choice)
which = 'Hello World'
while which != 'L' or which != 'F':
    which = input('\nWhich way would you like to report your profits'
                  '\n>>>').upper()
    if which == 'L' or which == 'LI' or which == 'LIF' or which == 'LIFO' or which == 'LF':
        choice = 'L'
        print("Okay you have chosen LIFO")
        break
    elif which == 'F' or which == 'FI' or which == 'FIF' or which == 'FIFO' or which == 'FF':
        choice = 'F'
        print("Okay you have chosen FIFO")
        break

# Explains how do interact with the menu
input("\nTo BUY shares to the list enter 1 or type BUY or B"
      "\nTo SELL shares from the list enter 2 or type SELL or S"
      "\nTo check the PROFIT made enter 3 or type PROFIT of P"
      "\nTo EXIT the program enter 4 or type EXIT or E"
      "\n\nPRESS ENTER")
# Menu
menu = 'Hello World'
while menu == 'Hello World':
    print("\nCurrent shares:", Shares)
    action = input("\n1. BUY"
                   "\n2. SELL"
                   "\n3. PROFIT"
                   "\n4. EXIT"
                   "\n>>>").upper()
# The user has to input the amount of shares bought and at what price
    if action == 'BUY' or action == '1' or action == "B":
        buy = 0
        while buy != "Hello World":
            buy = input("\nHow many shares do you wish to BUY?"
                        "\n>>>")
            try:
                buy = int(buy)
                break
            except ValueError:
                print("\nGive me a whole number please")

        cost = 0
        while cost != "Hello World":
            cost = input("\nHow much did you buy each share for?"
                         "\n>>>")
            try:
                cost = int(cost)
                break
            except ValueError:
                try:
                    cost = float(cost)
                    break
                except ValueError:
                    print("Give me a number please")

        # Adds these values to the Stack if chosen
        Shares += buy
        if choice == "L":
            MyStackShare.push(buy)
            MyCoSt.push(cost)

        # Adds these values to the Queue if chosen
        elif choice == "F":
            MyQueueShare.push(buy)
            MyQost.push(cost)

# They can sell that stock and state the price
    elif action == 'SELL' or action == '2' or action == "S":
        sell = 0
        while sell != "Hello World":
            sell = input("\nHow many shares do you wish to SELL?"
                         "\n>>>")
            try:
                sell = int(sell)
                break
            except ValueError:
                print("Type a whole number please")

        sold = 0
        while sold != 'Hello World':
            sold = input("How much did you SELL each share for?"
                         "\n>>>")
            try:
                sold = int(sold)
                break
            except ValueError:
                try:
                    sold = float(sold)
                except ValueError:
                    print("Enter a number please")

        if Shares < sell:
            print("You need to BUY more shares before you can SELL!")
        else:
            Shares -= sell
            sell1 = sell
            # If the user chose LIFO at the beginning this will sell the shares using the Stack
            if choice == "L":
                current = MyStackShare.head()
                if current == sell:
                    selling = sold * sell
                    bought = MyCoSt.head() * current
                    profit = selling - bought
                    Profit += profit
                    MyStackShare.pop()
                    MyCoSt.pop()
                    if profit > 0:
                        print(f"Your profit is ${profit}")
                    elif profit < 0:
                        print(f"You are at a loss of ${abs(profit)}")
                    else:
                        print("You have made no profit for these shares")

                elif current > sell:
                    current -= sell
                    selling = sold * sell
                    bought = MyCoSt.head() * sell
                    profit = selling - bought
                    Profit += profit
                    MyStackShare.pop()
                    MyStackShare.push(current)
                    if profit > 0:
                        print(f"The profit is ${profit}")
                    elif profit < 0:
                        print(f"You have a loss of ${abs(profit)}")
                    else:
                        print("You have made no profit for these shares")

                elif sell > current:
                    bought = []
                    while sell > current:
                        current = MyStackShare.head()
                        bought.append(MyCoSt.head() * current)
                        sell -= current
                        MyStackShare.pop()
                        MyCoSt.pop()
                        current = MyStackShare.head()

                        if current - sell > 0:
                            bought.append(sell * MyCoSt.head())
                            current -= sell
                            MyStackShare.pop()
                            MyStackShare.push(current)
                            break

                        elif current - sell == 0:
                            bought.append(sell * MyCoSt.head())
                            MyStackShare.pop()
                            MyCoSt.pop()
                            break
                    profit = (sold * sell1) - sum(bought)
                    Profit += profit
                    if profit > 0:
                        print(f"You have made a profit of ${profit}")
                    elif profit < 0:
                        print(f"Those shares put you at a loss of ${abs(profit)}")
                    else:
                        print("You have made no profit for these shares")

            elif choice == "F":
                # If the user chose FIFO at the beginning this will sell the shares using the Queue
                current = MyQueueShare.head()
                if current == sell:
                    selling = sold * current
                    bought = MyQost.head() * sell
                    profit = selling - bought
                    Profit += profit
                    MyQueueShare.pop()
                    MyQost.pop()
                    if profit > 0:
                        print(f"Your profit is ${profit}")
                    elif profit < 0:
                        print(f"You are at a loss of ${abs(profit)}")
                    else:
                        print("You have made no profit for these shares")

                elif current > sell:
                    current -= sell
                    selling = sold * sell
                    bought = MyQost.head() * sell
                    profit = selling - bought
                    Profit += profit
                    MyQueueShare.pop()
                    MyQueueShare.replace_head(current)
                    if profit > 0:
                        print(f"The profit is ${profit}")
                    elif profit < 0:
                        print(f"You have a loss of ${abs(profit)}")
                    else:
                        print("You have made no profit for these shares")

                elif sell > current:
                    bought = []
                    while sell > current:
                        current = MyQueueShare.head()
                        print('1')
                        print(sell)
                        print(current)
                        print(MyQost.head())
                        bought.append(MyQost.head() * current)
                        sell -= current
                        MyQueueShare.pop()
                        MyQost.pop()
                        current = MyQueueShare.head()

                        if current - sell > 0:
                            bought.append(MyQost.head() * sell)
                            current -= sell
                            MyQueueShare.pop()
                            MyQueueShare.replace_head(current)
                            break

                        elif current - sell == 0:
                            bought.append(MyQost.head() * sell)
                            MyQueueShare.pop()
                            MyQost.pop()
                            break
                    profit = sold * sell1 - sum(bought)
                    Profit += profit
                    if profit > 0:
                        print(f"You have made a profit of ${profit}")
                    elif profit < 0:
                        print(f"Those shares put you at a loss of ${abs(profit)}")
                    else:
                        print("You have made no profit for these shares")

    # This just returns the current profit to date
    elif action == "PROFIT" or action == '3' or action == "P":
        if Profit > 0:
            print(f"Your total profit is ${Profit}")
        elif Profit < 0:
            print(f"Looks like you have a loss of ${abs(Profit)}")
        else:
            print("You have made a total profit of... nothing."
                  "\nYour profit is sitting at $0")

    # Says bye and exits the program
    elif action == 'Exit' or action == '4' or action == "E":
        print("See you later")
        quit()
