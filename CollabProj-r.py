wrongGuesses = 1
#print("    |   ")
#print("    |   ")
if (wrongGuesses == 1):
  #print("   ()   ")
  print("\t|\n\t|\n\t()\n\t")
elif (wrongGuesses == 2):
  #print("\n\t/")
  print("\t|\n\t|\n\t()\n\t" + "/")
  print("2")
elif (wrongGuesses == 3):
  #print("\n\t/|")
  print("\t|\n\t|\n\t()\n\t" + "/|")
elif (wrongGuesses == 4):
  #print("\n\t/|\ ")
  print("\t|\n\t|\n\t()\n\t" + "/|\ \n\t")
elif (wrongGuesses == 5):
  #print("\n\t/")
  print("\t|\n\t|\n\t()\n\t" + "/|\ \n\t" +"/")
elif (wrongGuesses == 6):
  #print("\n\t /\\")
  print("\t|\n\t|\n\t()\n\t" + "/|\ \n\t" + "/\\")
else:
  print("DEV : Nonething wrong here")