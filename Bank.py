def show_balance(balance):
    print('*' * 25)
    print(f"Your balance is $ {balance:.2f}")
    print('*' * 25)

def deposit():
    print('*' * 25)
    amount = float(input('enter an amount to be deposited: '))
    print('*' * 25)
    if amount < 0:
        print('*' * 25)
        print("this is invalid amount:")
        print('*' * 25)
        return 0
    else:
        return amount


def withdraw(balance):
    print('*' * 25)
    amount = float(input('enter an amount to be withdraw: '))
    print('*' * 25)
    if amount > balance:
        print('*' * 25)
        print("Insufficient funds")
        print('*' * 25)
    elif amount < 0:
        print('*' * 25)
        print("amount must be greater than zero")
        print('*' * 25)
        return 0
    else:
        return amount


def main():
    balance = 0.0
    is_running = True
    while is_running:
        print('*' * 25)
        print("Banking System")
        print('*' * 25)
        print("1.show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print('*' * 25)
        choice = input('Enter Your choice from 1 : 4: ')
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print('*' * 25)
            print("Please enter valid choice: try again")
            print('*' * 25)
    print('THX PRO!')

if __name__ == '__main__':
    main()
