import random

MAX_REPS = 5
MAX_BET = 150
MIN_BET = 5

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_wins(columns, lines, bet, values):
    wins = 0
    win_reps = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            wins += values[symbol] * bet
            win_reps.append(line + 1)

    return wins, win_reps


def slot_spins(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def slot_print(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def getting_reps():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_REPS) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_REPS:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


def getting_bet():
    while True:
        amount = input("How many dollars will you bet?")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    lines = getting_reps()
    while True:
        bet = getting_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = slot_spins(ROWS, COLS, symbol_count)
    slot_print(slots)
    wins, win_reps = check_wins(slots, lines, bet, symbol_value)
    print(f"You won ${wins}.")
    print(f"You won on lines:", *win_reps)
    return wins - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"Now you left, its ${balance} yours ")


main()
