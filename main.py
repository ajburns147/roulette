# Allow spin function
import random

# Create an Overall win

# Set default bet sizes
start_bet = 25
current_bet = 25

# Reset roll counter
roll_number = 0

# Reset memory
past_1 = 2
past_2 = 2
past_3 = 2
past_4 = 2
past_5 = 2
# 0=Loss
# 1 = Won


# Set starting total money
money = 1000

# Start with Even
choose = 2468

# set min and max before leave table
while (1 <= money <= 2000):
    spin = random.randint(1, 38)  # spin

    if (past_1 == 0):  # double if lose
        current_bet *= 2

        # ability to switch between odd and even
        if (choose == 2468):
            choose = 1357
        elif (choose == 1357):
            choose = 2468

            # If win,reset bet
    elif (past_1 == 1):
        current_bet = start_bet

    # Don't bet more money than what you have
    if (current_bet >= money):
        current_bet = money

    # If good probability, half in
    if (past_1 + past_2 + past_3 + past_4 + past_5 == 0):
        current_bet = round(money)

    # Going for Odd(Start)
    if (choose == 1357):
        if (spin == 37 or spin == 38):
            money = money - current_bet
            print("Instant Loss")
            past_1 = 0

        elif (spin % 2 != 0):
            print("Odd")
            money = money + current_bet
            past_1 = 1
        else:
            print("Even")
            money = money - current_bet
            past_1 = 0





    # Going for Even
    elif (choose == 2468):
        if (spin == 37 or spin == 38):
            money = money - current_bet
            print("Instant Loss")
            past_1 = 0

        elif (spin % 2 != 0):
            print("Odd")
            money = money - current_bet
            past_1 = 0
        else:
            print("Even")
            money = money + current_bet
            past_1 = 1
    else:
        print("ERROR!!!")

        # store memory
    past_5 = past_4
    past_4 = past_3
    past_3 = past_2
    past_2 = past_1

    # roll counter
    roll_number += 1

    # print info
    print(roll_number, "= roll number")
    print("spin =", spin)
    print("$", money, "\n")
print("Earnings =", (money - 1000))