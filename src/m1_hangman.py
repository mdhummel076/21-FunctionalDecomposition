"""
Hangman.

Authors: Matt Hummel and James Werne.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DONE: 2. Implement Hangman using your Iterative Enhancement Plan.
import math
import random

def playHangman():

    print('------------------------------------------------------------------------------------')
    print(' |      |        |       |       |     ----    |         |       |       |       | ')
    print(' |      |       | |      | -     |   /      \  | -     - |      | |      | -     | ')
    print(' |      |      |   |     |  -    |  |          |  -   -  |     |   |     |  -    | ')
    print(' |------|     |-----|    |   -   |  |          |   - -   |    |-----|    |   -   | ')
    print(' |      |    |       |   |    -  |  |     ---- |    -    |   |       |   |    -  | ')
    print(' |      |   |         |  |     - |   \      /  |         |  |         |  |     - | ')
    print(' |      |  |           | |       |     -----   |         | |           | |       | ')
    print('------------------------------------------------------------------------------------')

    word = ''
    blankword =''
    Scount = 0
    Fcount = 0
    n = 11-int(input("Choose difficulty, 1-10:"))
    word = generateWord(word)
    blankword = generateBlankWord(word)
    printBlankword(blankword)
    while((Scount<len(word)) & (Fcount < n)):
        guessed = guessWord(word,blankword)
        if(guessed > 0):
            Scount += guessed
            printBlankword(blankword)
        else:
            Fcount += 1
            print("Letter not in word, you have "+str(n-Fcount)+' attempts remaining')
            printBlankword(blankword)
    if(Scount>=len(word)):
        print("You Win!")
    else:
        print("You Lose, the word was: "+word)






def generateWord(word):
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
        ourword = words[random.randrange(0,len(words))]
        for k in range(len(ourword)):
            word += ourword[k]
    return word

def generateBlankWord(word):
    blankword = []
    for k in range(len(word)):
        blankword += ['_']
    return blankword

def guessWord(word,blankword):
    letter = input("Give me a letter")
    count = 0
    for k in range(len(word)):
        if(word[k]==letter[0]):
            fillInWord(blankword,word,letter)
            count += 1
    return count

def fillInWord(blankword,word,letter):
    for j in range(len(word)):
        if(word[j]==letter):
            blankword[j] = letter

def printBlankword(blankword):
    for k in range(len(blankword)):
        print(blankword[k],end = '')
        print(' ',end='')
    print('')


playHangman()

####### Do NOT attempt this assignment before class! #######

