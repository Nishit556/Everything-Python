print("welcome to the Iron Bank of Belaroos ATM")
restart = ('y')
chances = 3
balance = 69.83
while chances >= 0:
    pin = int(input('PLease Enter the 4 Digit PIN: '))
    if pin == (1234):
        print("You entered your pin correctly\n")
        while restart not in ('n', 'NO', 'no', 'N'):
            print('Please Press 1 For Your Balance')
            print('PLease Press 2 To Make a Widhraw')
            print('Please Press 3 To Pay')
            print('PLease press 4 To Return')
            option = int(input("What would you like to choose?"))
            if option == 1:
                print('Your Balance is: ', balance,'\n')
                restart = input('Would you like to go back?')
                if restart in ('n', 'NO', 'no', 'N'):
                    print("Thank You")
                    break
            elif option == 2:
                    option2 = ('y')
                    withdrawal = float(input("How much Would you like to withdraw?"))
                    if withdrawal in [10, 20, 40, 60, 80, 100]:
                        balance = balance - withdrawal
                        print("Your Balance is now: ", balance)
                        restart = input("Would you like to go back?")
                        if restart in('no', ' NO', 'no', 'N'):
                            print('Thank You')
                            break
                    elif withdrawal != [10, 20, 30, 40, 60, 80, 100]:
                        print("Invalid AMount, PLease RE-ENTER the Amount\n")
                        restart = ('y')
                    elif withdrawal == 1:
                        withdrawal = float(input("Please enter desired amount"))
            elif option == 3:
                    Pay_in = float(input('How much would you like to Pay In?'))
                    balance = balance + Pay_in
                    print("Your balance is now: ",balance)
                    restart = input("Would you like to go back?")
                    if restart in ('no', ' NO', 'no', 'N'):
                        print("Thank You")
                        break
            elif option == 4:
                    print("Thank you for your service")
                    break
            else:
                print("Enter a correct number.")
                restart = ('y')
    elif pin != ('1234'):
        print("Incoorect Pin")
        chances = chances - 1
        if chances == 0:
            print("No more tries")
            break