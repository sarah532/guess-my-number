guess = 0
high = 100
low = 0
guess = int((high+low)/2)
newGuess  = int()

print ('Please think of a number between 0 and 100!')
answer = ('')


while True :

    print ('Is ' + str(guess) + ' your secret number?' + ' Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly. Enter "h" to indicate guess it too h')
    answer = str(input())
    if answer == 'l': 
       guess = abs((high+guess)/2)
       low = guess
        
    elif answer == 'h':
        guess = (low+guess)/2
        high = guess
    elif answer == 'c':
        print(str(guess) + ' is the right answer!')            
        break
    else:
        print('Sorry, I did not understand your input.')