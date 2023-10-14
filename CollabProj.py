#APCSP Create Task - Carreon,Matthew in collboration with Magdangal,Vinpatrik (Student taking APCSP)

import random

#Selection of words, feel free to change whenever
wordList = ["test","computer","science","stickman","funny","foo","bar","lucky","world","pixel","python"]

#Taken from geeksforgeeks.org
def wordSplit(word):
    return [char for char in word]

#####################################################################################
#                                                                                   #
#                Visuals for the stickman itself based off wrong guesses            #
#                                                                                   #
#####################################################################################

def checkWrongGuess (num):
  if (num == 1):
    #print("   ()   ")
    print("\t|\n\t|\n\t()\n\t")
  elif (num == 2):
    #print("\n\t/")
    print("\t|\n\t|\n\t()\n\t" + "/")
    #print("2")
  elif (num == 3):
    #print("\n\t/|")
    print("\t|\n\t|\n\t()\n\t" + "/|")
  elif (num == 4):
    #print("\n\t/|\ ")
    print("\t|\n\t|\n\t()\n\t" + "/|\ \n\t")
  elif (num == 5):
    #print("\n\t/")
    print("\t|\n\t|\n\t()\n\t" + "/|\ \n\t" +"/")
  elif (num == 6):
    #print("\n\t /\\")
    print("\t|\n\t|\n\t()\n\t" + "/|\ \n\t" + "/\\")
  else:
    #print("DEV : Nothing wrong here")
    print("")
    #Could be better...

#####################################################################################
#                                                                                   #
#    This section splits a randomly selected word and creates the blank spaces      #
#                                                                                   #
#####################################################################################

#Adds each character in the selected word into a list
wordListSelection = random.choice(wordList)
#Ensure if there is a capitlization in wordList the user is able to still continue
wordListSelection = wordListSelection.lower()
selectedWord = (wordSplit(wordListSelection))

#print("DEV TEST: The correct answer for selectedWord (list) is:" + str(selectedWord) + "\n")

#shownList is the characters inputted by the user
shownList = []
for x in range(0, len(selectedWord)):
  shownList.append("_")
print("You need to guess this word: " + str(shownList))


#####################################################################################
#                                                                                   #
#                   This is where the guessing part starts                          #
#                                                                                   #
#####################################################################################

guessCounter = 0
guessedLetters = []
youWin = bool(False)
underscoreCount = len(selectedWord)
properGuess = bool(False)
matchingLetters = 0
wrongGuesses = 0
youLose = bool(False)
gameEnd = bool(False)
dupeLetters = 0


#runs until the number of guesses reaches 6 or you win
while gameEnd == False:
 dupeLetters = 0
 #print("TEST: THERE ARE " + str(underscoreCount) + " UNDERSCORES LEFT")
 guess = input("\nPlease guess a letter: ")
 properGuess = False
 #checks if the guess is too long, has a non-alpha character, and is capital
 if len(guess) > 1:
    print("This guess is too long! Please try again.")
 elif str.isupper(guess) == True:
   print("Do not use an uppercase letter! Please try again.")
 elif str.isalpha(guess) == False:
   print("Please only use letters! Please try again")
#looks for duplicate letter inputs
 elif guessCounter >= 1:
   for x in range(0,len(guessedLetters)):
     if guess == guessedLetters[x]:
       dupeLetters += 1
     else:
       dupeLetters += 0
   if dupeLetters == 0:
      properGuess = True
   else:
     print("You already used that letter!")
     properGuess = False
 else:
   properGuess = True
  

 #only runs this section if the user makes a proper guess  
 if properGuess == True:
    matchingLetters = 0
    guessedLetters.append(guess)
    guessCounter += 1

    #Shows the previous inputs and inserts where the proper char. should be
    print("You guessed the letters: " + str(guessedLetters))
    for num in range(0,len(shownList)):
      if guess == selectedWord[num]:
        del shownList[num]
        shownList.insert(num, guess)
        matchingLetters += 1

        #print("TEST: NOW DOING THE EQUATION " + str(underscoreCount) + " - " + str(matchingLetters))
        underscoreCount = underscoreCount - 1

        #if there is an underscore, it keeps going
        for num in range(0,len(shownList)):
          if "_" == shownList[num]:
            #print("DEV IF: selectedWord[num] is " + str(selectedWord[num]))
            #print("There is an underscore.")
            youWin = False
          else:
            #print("DEV ELSE: selectedWord[num] is " + str(selectedWord[num]))
            #print("There is no underscore.")
            if (underscoreCount == 0):
              #if statement to make sure "test" works and to prevent the condition to become true if an underscore is detected
              youWin = True
              gameEnd = True
              #print("LINE 125-127 IS RUNNING")

    print(shownList)
    if matchingLetters > 0:
      continue
    else:
      wrongGuesses += 1
      #print("TEST: THERE IS A WRONG GUESS" + " VALUE OF MATCHING LETTER IS " + str(matchingLetters))
    if wrongGuesses == 1:
      print("You have " + str(wrongGuesses) + " incorrect guess.")
    else:
      print("You have " + str(wrongGuesses) + " incorrect guesses")
    checkWrongGuess(wrongGuesses)
    if wrongGuesses == 6:
      youLose = True
      gameEnd = True
      #print("LINE 143-145 IS RUNNING")
    
#Winning or Losing statement at the end of the game
if youWin == True: 
  print("\nYou won! Yay!")
else:
  print("Game over.")
  print("The word was " + wordListSelection + ".")








######################################################################################
#                                  CHANGELOG                                         #
######################################################################################
"""
4/28: Changed if else selectedWord to shownList (Fixed the loop), Added underscoreCount for a failsafe, Added Hangman Visual(concept) - M
"""

"""
4/29: Added feature that only accepts lowercase letters and lets the user try again - V
"""

"""
5/3: Implemented Dupe checker for the input and visuals for stickman and the lose condition
"""