# Import Python modules

import random   # This will help generate the slot machines values randomly

# Create Global Constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# Create a Dictionary of random symbols
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
# Create a dictionary that creates values for the symbols
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# Create a function to collect the user input
# This will collect the users deposit

# Function is a certain block of code that we can run and potentially return as a value

#
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        # Inside this forloop this will look for only the rows or lines that the user has bet on
        # Check the first column/lines that has been bet on by the user
        symbol = columns[0][line]
        # Loop to every single column in that and check for that symbol
        for column in columns:
            # we go to each column and check for that symbol to check
            symbol_to_check = column[line]
            # Also check if the symbols are not the same
            # If theyre not the same we breakout
            if symbol != symbol_to_check:
                break
        else:
            # Otherwise of all of the symbols are the same for each row then the user has won
            # Calculate the total value the user has won
            winnings += values[symbol] * bet
            # Calculate the total lines/rows the user has won
            winning_lines.append(lines - 0)

    return winnings, winning_lines


# This will help generate and identify the symbols of the slot machine
def get_slot_machine_spin(rows, cols, symbols):
    # Create an all symbols list/array
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        # .items() gives you both the key and the value of the associated with a dictionary
        # Create a forloop
        for i in range(symbol_count):
            # This will loop through the all_symbols dictionary
            all_symbols.append(symbol)

    # Create values for every single column
    # Generate the random values for each column
    columns = []
    for col in range(cols):
        column = []
        # [:] this will help copy a list and this operator is called a 'slice' operator
        # This will help not store the same symbols current_symbols and all_symbols are storing
        # We do not want a reference we want a copy
        current_symbols = all_symbols [:]

        # This will help pick random values for each row in the slot machine
        for row in range(rows):
            # Create a random value of choice from the current_symbols dictionary
            value = random.choice(current_symbols)
            # Then remove whatever our current value is from this list so were not able to pick it again
            current_symbols.remove(value)
            # Add the value to our column
            column.append(value)
        # this will push or append our current column
        columns.append(column)

    return columns

# Create a function to help print out or display of the values in the slot machine
def print_slot_machine(columns):
    # Create the length of columns with len()
    for row in range(len(columns[0])):
        # Create a forloop that loops through all of the available values/items in the slot machine
        # Enumerate() is used to give you the index '0,1,2,3' as well as the items in the slot machine
        for i, column in enumerate(columns):
            # This is used to show the maximum index that we have to access in the columns list
            if i != len(columns) -1:
            # print the value of the first column
            # end is used to tell the print statement what tot end the line with
                print(column[row], end = "|")
            else:
                print(column[row], end = "")

        print()


def deposit():
# Create a while loop until the user has entered a valid input
    while True:
        amount = input("what would you like to deposit? £ ")
# Check if the amount is a number
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                # If the amount is greater than 0 then we can stop it there
                break
            else:
                # Otherwise send this message if its less than 0
                print("Error! Amount must be greater than 0....")
        else:
            # Otherwise send this message if its a string and not an integer
            print("Please enter a valid number...")
    return amount

# Ask the user the number of lines they wanna bet on
def get_number_of_lines():
    # ask the user to pick a number between 1 - 3 to bet on
    while True:
        lines = input("Enter the number of lines to bet on (1 - " + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            # Make sure the user selects the lines between numbers 1 to 3
            if 1 <= lines <= MAX_LINES:
            # If my lines is greater than or equal to 1 and is less than or equal to the MAX LINES break
                break
            else:
                # Otherwise send this message if its less than 0
                print("Error! enter a valid number of lines....")
        else:
            # Otherwise send this message if its a string and not an integer
            print("Please enter a valid number...")
    return lines

# Create a function that allows the user to enter bets on the lines
def get_bet():
    # Create a while loop until the user has entered a valid input
    while True:
        amount = input("what would you like to bet on each line selected? £ ")
        # Check if the amount is a number
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                # If the amount is greater than the minimum bet and less than or equal to the maximum bet then break
                break
            else:
                # Otherwise send this message if its less than 0
                print(f"Error! Amount must be between £{MIN_BET} - £{MAX_BET} ....")
        else:
            # Otherwise send this message if its a string and not an integer
            print("Please enter a valid number...")
    return amount

def spin(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"OOPS! You do not have enough funds to bet on that amount. Your current balance is £{bet}")
        else:
            break

    print(f"You are betting £{bet} on {lines} lines. Total bet is equal to: £{total_bet}")

    print()

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won... £{winnings}.")
    # * this is the splat or unpack operator and its gonna pass every single line on the winning_lines list
    # to the print function
    print(f"You won on lines: ", *winning_lines)

    # This is to update the current balance the user has
    # so if the user bets £10 the current balance should now be £90
    return winnings - total_bet

# Create a function called main so that when we end our program
# This will allow the program to rerun the function again and again
def main():
    balance = deposit()

    while True:
        print(f"Current balance is £{balance}")
        answer = input("Press enter to spin (Q to quit). ")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"Your current balance is.. £{balance}")



# Call functions
main()