import random
SecretNumber=random.randrange(0,1000)
Name=input('What is your name?: ')
print('Hello '+Name+', im thinking on an integer between 0 and 1000, take a guess:')
for GuessesTaken in range(1,11):
    #print('DEBUG:'+str(SecretNumber))
    print('Tries left:'+str(11-GuessesTaken))
    while True:
        try:
            Guess=input()
            Check=int(Guess)
            break
        except:
            print('You must type a valid number')
    
    if int(Guess)<SecretNumber:
        print('Too low')
    elif int(Guess)>SecretNumber:
        print('Too high')
    else:
        break
if GuessesTaken==10:
    print('You ran out of tries')
else:
    print('That is the number, congrats!')

    
