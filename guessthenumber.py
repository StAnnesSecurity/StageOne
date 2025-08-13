x = 50

guess = input('Guess the number between 1 and 100: ')

if float(guess) <= (x - 10):
    print('Ice Cold! Maybe next time.')
else: 
    if float(guess) >= (x + 10):
        print('Ice Cold! Maybe next time.')
    else:
        if float(guess) <= (x - 5):
            print('Cold! Maybe next time.')
        else:
            if float(guess) >= (x + 5):
                print('Cold! Maybe next time.')
            else:
                if float(guess) <= (x - 3):
                    print('Warm! Maybe next time.')
                else:
                    if float(guess) >= (x + 3):
                        print('Warm! Maybe next time.')
                    else:
                        if float(guess) <= (x - 1):
                            print('Hot! Maybe next time.')
                        else:
                            if float(guess) >= (x + 1):
                                print('Hot! Maybe next time.')
                            else:
                                print('You got it!')
    