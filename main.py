import time
import random


wordList = ["dog", "cat", "house"]
#guesses = 

#Procedures
def randomWord(words):
  chosenWord = words[random.randint(0, len(words)-1)]
  print("DEBUG: the word chosen is at " + chosenWord)
  return chosenWord

#main
print("Welcome to hangman user!")
print("Hangman is where you guess the letter by typing it in")
print("Becareful though")
print("    |   ")
print("    |   ")
print("   ()   ")
print("   /|\    ")
print("   /\    ")
wordChose = randomWord(wordList)
print(wordChose)