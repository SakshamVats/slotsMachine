from os import _exit
import random
import math

MAX_LINES = 3
MAX_BET_PER_LINE = 100
ROWS = 3
COLS = 3

def get_deposit():
    while True:
        deposit = input("Enter deposit amount: $")
        if deposit.isdigit():
            if int(deposit) > 0:
                break
            else:
                print("Enter positive amount.")
        else:
            print("Enter numeric amount.")

    return int(deposit)

def get_bet_lines():
    while True:
        bet_lines = input("Enter number of lines to bet on, or 'q' to quit: ")
        if str(bet_lines) == 'q':
            exit()
        if bet_lines.isdigit():
            if 0 < int(bet_lines) <= MAX_LINES:
                break
            else:
                print(f"Enter number between 0 and {MAX_LINES + 1}.")
        else:
            print("Enter numeric amount.")

    return int(bet_lines)

def get_bet_per_line():
    while True:
        bet_per_line = input("Enter bet per line: ")
        if bet_per_line.isdigit():
            if 0 < int(bet_per_line) <= MAX_BET_PER_LINE:
                break
            else:
                print(f"Enter number between 0 and {MAX_BET_PER_LINE + 1}.")
        else:
            print("Enter numeric amount.")

    return int(bet_per_line)

def get_transpose(matrix):
    return [[x[i] for x in matrix] for i in range(len(matrix[0]))]

def get_slots(rows, cols, symbols_list):
    slots = []
    for _ in range(cols):
        symbols_available = symbols_list[:]
        column = []
        for _ in range(rows):
            symbol_chosen = random.choice(symbols_available)
            column.append(symbol_chosen)
            symbols_available.remove(symbol_chosen)
        slots.append(column)
    
    return slots

def get_prize(spin, bet_lines, prize_dict):
    spin_transpose = get_transpose(spin)
    for row in spin_transpose:
        print(' | '.join(map(str, row)))

    prize = 0
    for line in range(bet_lines):
        current_line = spin_transpose[line]
        if len(set(current_line)) <= 1:
            prize += prize_dict[current_line[0]]
    return prize

def main():
    symbols_dict = {
        'A' : 3,
        'B' : 4,
        'C' : 5,
        'D' : 6
        }

    prize_dict = {
        'A' : 10,
        'B' : 6,
        'C' : 4,
        'D' : 2
        }

    symbols_list = []
    for key, value in symbols_dict.items():
        for _ in range(value):    
            symbols_list.append(key)

    #print(symbols_list)
    
    balance = get_deposit()
    while True:
        bet_lines = get_bet_lines()
    
        bet_per_line = get_bet_per_line()
        while bet_lines * bet_per_line > balance:
            print("You don't have enough balance. Bet a lower amount.")
            bet_per_line = get_bet_per_line()

        balance -= bet_lines * bet_per_line

        spin = get_slots(ROWS, COLS, symbols_list)
        prize = get_prize(spin, bet_lines, prize_dict)
        if prize > 0:
            print(f"You won ${prize}!")
        else:
            print("Whoops! You didn't win anything")

        balance += prize*bet_per_line
        print(f"You now have ${balance}.")

        if balance <= 0:
            print("You ran out of money!")
            break

main()