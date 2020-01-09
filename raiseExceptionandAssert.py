def oneCharacter():
    symbol=input('Enter only one character\n')
    assert len(symbol)==1,'I told you one character'
    print('EXCELENT!')

def multipleCharacters():
    symbols=input('Enter more than one character\n')
    if len(symbols)<2:
        raise Exception('You should enter more than one character')
    else:
        print('Success!')

oneCharacter()
multipleCharacters()
