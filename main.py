import time
import os 
'''https://docs.python.org/3/library/os.html && https://www.w3resource.com/python-exercises/python-basic-exercise-99.php (clear terminal)'''
import random

#Procedures
def randomWord(words):
  chosenWord = words[random.randint(0, len(words)-1)]
  print("DEBUG: the word chosen is at " + chosenWord)
  return chosenWord

def wipeScreen():
  os.system('cls')

def indexWord(wordChosen):
  index = []
  for letter in wordChosen:
    index.append(letter)
  return index

def letterCheck(word):
  for i in range(0, len(word)-1):
    print(Test)
    print("    |   ")
    print("    |   ")
    print("   ()   ")
    print("   /|\    ")
    print("   /\    ")

#Variables
wordList = ["house", "design", "export", "market", "resort", "winner"]
wordLetterIndex = [""]
numOfGuesses = 0
wrongGuesses = 0
name = ""
#main

name = input("What is your name?\n")
print("Welcome to hangman " + name + "!" )
print("Hangman is where you guess the letter by typing it in")
print("Becareful though as it slowly creates a stickfigure when guessing incorrectly!")
wordChose = randomWord(wordList)
print(wordChose)
wordLetterIndex = indexWord(wordChose)
print("Debug: Index of the chosen word is ")
'''for x in wordLetterIndex:
  print(x)'''
