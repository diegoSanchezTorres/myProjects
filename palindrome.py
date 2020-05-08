def ispalindrome(word):
    #Eliminates spaces
    wordNoBlanks=''
    for letter in word:
        if letter == ' ':
            continue
        wordNoBlanks+=letter
    #Reverse Word
    wordlist=list(wordNoBlanks)
    wordlist.reverse()
    word2="".join(wordlist)
    #Compare words
    if wordNoBlanks==word2:
        return True
    else:
        return False
    
    
    
    


if ispalindrome('anita lava la tina') is True:
    print('Es palindromo')
else:
    print('No es palindromo')
