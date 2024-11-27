import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count = {

    "$" : 3, 
    "@" : 4,
    "#" : 6,
    "&" : 7,
}

symbol_value = {
    "$" : 5, 
    "@" : 4,
    "#" : 3,
    "&" : 2,    
}

def check_winnings(columns , lines, bet, values):

    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns :
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]* bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def slot_machine_spin(rows, cols, symbols):

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

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:

                print(column[row], end = " | ")
            else:
                print(column[row], end= "")
        
        print()

def deposite():

    while True:
        amount = input("How much you want to deposite ?: $")

        if amount.isdigit():
            amount = int(amount)

            if amount > 0:
                break
            else:
                print("Amount must be > then 0")
        else:
            print("Please enter a valid Amount.")
    
    return amount

def get_num_of_line():

    while True:
        lines = input("Enter the number of lines to bet on (1- "+ str(MAX_LINES)+")? ")
 
        if lines.isdigit():
            lines = int(lines)

            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid line")
        else:
            print("Please enter a valid Number.")
    
    return lines

def get_bet():

    while True:
        amount = input("How much would you like to BET on each Lines ?:  ")
 
        if amount.isdigit():
            amount = int(amount)

            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET}- {MAX_BET}.")
        else:
            print("Please enter a valid Number.")
    
    return amount

def spin(balance):

    lines = get_num_of_line()
    while True :

        bet = get_bet()
        total_bet = bet*lines
        if total_bet > balance :
            print(f" Unable to bet , YOUR CURRENT BALANCE : ${balance} ")
        else:
            break


    print(f"You are betting {bet} on {lines} lines. Total Bet : {total_bet}.")

    slots = slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f" You won ${winnings}.")
    print(f"You won on lines: ", *winning_lines)

    return winnings - total_bet

def main():

    balance = deposite()
    while True :
        print(f"Current Balance is: ${balance}")
        ans = input("Press enter to spin or Q to Quit. ")
        if ans == "q":
            break 
        balance += spin(balance)

    print(f"You Current Balance is ${balance}")
main()