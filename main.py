import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "@": 2,
    "#": 4,
    "$": 6,
    "%": 8
}

symbol_values = {
    "@": 5,
    "#": 4,
    "$": 3,
    "%": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines



def get_slot_machine_spin(rows, cols, symbols):
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
            print(column[row], "| " if i != len(columns)-1 else "", end="")

        print()


def deposit():
    while True:
        amount = input("Quanto quer depositar? R$ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("O valor tem que ser acima de 0.")
        else:
            print("Por favor, insira um número.")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Insira quantas linhas quer apostar (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Insira um valor válido de linhas.")
        else:
            print("Por favor, insira um número.")

    return lines


def get_bet():
    while True:
        amount = input("Quanto quer apostar em cada linha? R$ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("O valor tem que estar entre R$ {} e R$ {}.".format(MIN_BET, MAX_BET))
        else:
            print("Por favor, insira um número.")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print("Você não tem saldo o suficiente para esta aposta. Seu saldo atual é R$ {}".format(balance))
        else:
            break

    print("Você está apostando R$ {} em {} linha(s). Total da aposta: R$ {}".format(bet, lines, total_bet))

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print("Você acertou {}".format(winnings))
    print("Acertou em: ", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print("Saldo atual é de R$ {}".format(balance))
        spinkey = input("Aperte enter para girar (q para sair).")
        if spinkey == 'q':
            break
        balance += spin(balance)

    print("Saldo restante: R$ {}".format(balance))



main()
