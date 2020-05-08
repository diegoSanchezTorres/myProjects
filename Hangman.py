#Hangman_game
#Globals
word_complete=False
lifes=8
answer="bicycle"
answer=answer.lower()
incomplete_answer=[]
#Body

for x in answer:
    incomplete_answer.append("_")


print("Welcome to the Hangman game")
while(word_complete==False):
    print(" ".join(incomplete_answer))
    incomplete_answer=list(incomplete_answer)
    print("You have "+str(lifes)+" tries")
    guess=input("Guess a letter or the complete word: ")
    guess=guess.lower()
    for index,letter in enumerate(answer):
        if letter==guess:
            if letter in incomplete_answer:
                print("Already said that")
            incomplete_answer[index]=guess              
    if answer==str("".join(incomplete_answer)):
        word_complete=True
        print("You win!")

    guess=guess.lower()
    if guess in answer:
        print("Nice")
    else:
        lifes-=1
        if lifes==0:
            print("Game Over")
            break
    
