x = 50

while True :
    start = input('Guess the number between 1 and 100: ')
    
    try:
        guess = float(start)
    except:
        print('Invalid Input')
        continue

    if float(guess) == x :
        break

    else: 
        if guess <= (x - 30):
            print('Ice Cold! Try again.')
        else: 
            if guess >= (x + 30):
                print('Ice Cold! Try again.')
            else:
                if guess <= (x - 25):
                    print('Cold! Try again.')
                else:
                    if guess >= (x + 25):
                        print('Cold! Try again.')
                    else:
                        if guess <= (x - 15):
                            print('Warm! Try again.')
                        else:
                            if guess >= (x + 15):
                                print('Warm! Try again.')
                            else:
                                if guess <= (x - 5):
                                    print('Hot! Try again.')
                                else:
                                    if guess >= (x + 5):
                                        print('Hot! Try again.')

print('You got it!')
    