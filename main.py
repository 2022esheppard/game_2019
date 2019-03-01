import random
#Creating functions in order to allow the user to go back and forth between choosing home and choosing a game
#For hangman variable
def hangman():
    print("Good choice! It is recomended to keep track of your guesses and the placement of the correct letters on a piece of paper but not required. ")
    #List of choice of words that the user will end up interacting with in the game
    hmwordchoice = ['brave', 'learn', 'crazy', 'graze', 'quick' ]
    #random choice of one of the words to make sure that the user will get different words if they play a multitude of times
    finalhmword = (random.choice(hmwordchoice))

    #For the chosen word BRAVE
    if finalhmword == 'brave' :
      #Make the guesses that the user has for the letters into a function so that they can make multiple guesses
      def braveguess():
        #The amount of letters in the word printed
        print("__ __ __ __ __")
        #as a variable in order to count when the user has guessed all the letters correctly
        counter = 5
        #Keeping track of the amount of correct guesses have been made and making sure that the while loop stops when the full word has been guessed
        while counter != 0:
          guessbrave = input("Guess a letter:")
          #Things that should happen when the user guesses the right letter:
          if guessbrave == 'b':
            counter = (counter-1)
            print("That is the first letter of your word")
          elif guessbrave == 'r':
            counter = (counter-1)
            print("That is the second letter of your word")
          elif guessbrave == 'a':
            counter = (counter-1)
            print("That is the third letter of your word")
          elif guessbrave == 'v':
            counter = (counter-1)
            print("That is the fourth letter of your word")
          elif guessbrave == 'e':
            counter = (counter-1)
            print("That is the last letter of your word")
          #What should happen if the user guesses the wrong letter
          else:
            print("That letter is not in your word")
          #What should happen once the user has figured out the entire word
          if counter == 0 :
            print("Congrats you have figured out your word: BRAVE")
      #Calling the guessing function for the word brave
      braveguess()
      #Getting the user back to the home page once the game has been completed
      home()

    #For the chosen word LEARN
    elif finalhmword == 'learn' :
      #Make the guesses that the user has for the letters into a function so that they can make multiple guesses
      def learnguess():
        #The amount of letters in the word printed
        print("__ __ __ __ __")
        #as a variable in order to count when the user has guessed all the letters correctly
        counter = 5
        #Keeping track of the amount of correct guesses have been made and making sure that the while loop stops when the full word has been guessed
        while counter != 0:
          guesslearn = input("Guess a letter:")
          #Things that should happen when the user guesses the right letter:
          if guesslearn == 'l':
            counter = (counter-1)
            print("That is the first letter of your word")
          elif guesslearn == 'e':
            counter = (counter-1)
            print("That is the second letter of your word")
          elif guesslearn == 'a':
            counter = (counter-1)
            print("That is the third letter of your word")
          elif guesslearn == 'r':
            counter = (counter-1)
            print("That is the fourth letter of your word")
          elif guesslearn == 'n':
            counter = (counter-1)
            print("That is the last letter of your word")
          #What should happen if the user guesses the wrong letter
          else:
            print("That letter is not in your word")
          #What should happen once the user has figured out the entire word
          if counter == 0 :
            print("Congrats you have figured out your word: LEARN")
      #Calling the guessing function for the word learn
      learnguess()
      #Getting the user back to the home page once the game has been completed
      home()

    #For the chosen word CRAZY
    elif finalhmword == 'crazy' :
      #Make the guesses that the user has for the letters into a function so that they can make multiple guesses
      def crazyguess():
        #The amount of letters in the word printed
        print("__ __ __ __ __")
        #as a variable in order to count when the user has guessed all the letters correctly
        counter = 5
        #Keeping track of the amount of correct guesses have been made and making sure that the while loop stops when the full word has been guessed
        while counter != 0:
          guesscrazy = input("Guess a letter:")
          #Things that should happen when the user guesses the right letter:
          if guesscrazy == 'c':
            counter = (counter-1)
            print("That is the first letter of your word")
          elif guesscrazy == 'r':
            counter = (counter-1)
            print("That is the second letter of your word")
          elif guesscrazy == 'a':
            counter = (counter-1)
            print("That is the third letter of your word")
          elif guesscrazy == 'z':
            counter = (counter-1)
            print("That is the fourth letter of your word")
          elif guesscrazy == 'y':
            counter = (counter-1)
            print("That is the last letter of your word")
          #What should happen if the user guesses the wrong letter
          else:
            print("That letter is not in your word")
          #What should happen once the user has figured out the entire word
          if counter == 0 :
            print("Congrats you have figured out your word: CRAZY")
      #Calling the guessing function for the word crazy
      crazyguess()
      #Getting the user back to the home page once the game has been completed
      home()


    #For the chosen word GRAZE
    elif finalhmword == 'graze' :
      #Make the guesses that the user has for the letters into a function so that they can make multiple guesses
      def grazeguess():
        #The amount of letters in the word printed
        print("__ __ __ __ __")
        #as a variable in order to count when the user has guessed all the letters correctly
        counter = 5
        #Keeping track of the amount of correct guesses have been made and making sure that the while loop stops when the full word has been guessed
        while counter != 0:
          guessgraze = input("Guess a letter:")
          #Things that should happen when the user guesses the right letter:
          if guessgraze == 'g':
            counter = (counter-1)
            print("That is the first letter of your word")
          elif guessgraze == 'r':
            counter = (counter-1)
            print("That is the second letter of your word")
          elif guessgraze == 'a':
            counter = (counter-1)
            print("That is the third letter of your word")
          elif guessgraze == 'z':
            counter = (counter-1)
            print("That is the fourth letter of your word")
          elif guessgraze == 'e':
            counter = (counter-1)
            print("That is the last letter of your word")
          #What should happen if the user guesses the wrong letter
          else:
            print("That letter is not in your word")
          #What should happen once the user has figured out the entire word
          if counter == 0 :
            print("Congrats you have figured out your word: GRAZE")
      #Calling the guessing function for the word graze
      grazeguess()
      #Getting the user back to the home page once the game has been completed
      home()

    #For the chosen word QUICK
    elif finalhmword == 'quick' :
      #Make the guesses that the user has for the letters into a function so that they can make multiple guesses
      def quickguess():
        #The amount of letters in the word printed
        print("__ __ __ __ __")
        #as a variable in order to count when the user has guessed all the letters correctly
        counter = 5
        #Keeping track of the amount of correct guesses have been made and making sure that the while loop stops when the full word has been guessed
        while counter != 0:
          guessquick = input("Guess a letter:")
          #Things that should happen when the user guesses the right letter:
          if guessquick == 'q':
            counter = (counter-1)
            print("That is the first letter of your word")
          elif guessquick == 'u':
            counter = (counter-1)
            print("That is the second letter of your word")
          elif guessquick == 'i':
            counter = (counter-1)
            print("That is the third letter of your word")
          elif guessquick == 'c':
            counter = (counter-1)
            print("That is the fourth letter of your word")
          elif guessquick == 'k':
            counter = (counter-1)
            print("That is the last letter of your word")
          #What should happen if the user guesses the wrong letter
          else:
            print("That letter is not in your word")
          #What should happen once the user has figured out the entire word
          if counter == 0 :
            print("Congrats you have figured out your word: QUICK")
      #Calling the guessing function for the word quick
      quickguess()
      #Getting the user back to the home page once the game has been completed
      home()


#For madlibs variable
def madlibs():
    print("Good choice", name)
    #insuring that the user won't end up playing the same game over and over again
    mloptions = ("holiday", "school", "pet")
    mlchoice = random.choice(mloptions)
    #First madlibs option
    if mlchoice == 'holiday' :
      #Variables
      occupation1 = input("occupation:")
      holiday1 = input("holiday:")
      adjective1 = input("adjective:")
      verb1 = input("verb:")
      pluralnoun1 = input("plural noun:")
      singularnoun1 = input("singular noun:")
      adjective11 = input("adjective:")
      singularnoun11 = input("singular noun:")
      familymember1 = input("family member:")
      location1 = input("location:")
      adjective111 = input("adjective:")
      #Final product with the users input
      print ("My", occupation1, "came to visit us on", holiday1, ". It was very", adjective1, "because he likes to", verb1, "a lot more than the average person. He decided that we should eat", pluralnoun1,"instead of what we had planned. He also happened to bring with a",singularnoun1,"which he gave to my father and he also had a",adjective11, singularnoun11,"that somehow ended up in my", familymember1,"’s",location1,". When he left we were all",adjective111)

      print ("Thank you for doing this madlibs")
      #Allow user  to access the home page in order to play the same or other games
      mlchoiceofhomvgame = input("If you would like to do another madlibs write 'madlibs', if you would like to choose another game write 'home'.")
      if mlchoiceofhomvgame == 'madlibs' :
          madlibs()
      elif mlchoiceofhomvgame == 'home' :
          home()

    #The second madlibs option, about a pe tor other form of creature that the user takes care of
    elif mlchoice == 'pet' :
      #Variables
      adjective3 = input("adjective:")
      noun3= input("noun:")
      verb3 = input("verb:")
      adjective33 = input("adjective:")
      pluralnoun3= input("plural noun:")
      adjective333 = input("adjective:")
      pluralnoun33 = input("plural noun:")
      bodypart3 = input("body part:")
      noun33 = input("noun:")
      amountoftime3 = input("amount of time:")
      location3 = input("location:")
      adjective3333 = input("adjective:")
      verb33 = input("verb:")
      #Final product with the users input
      print("On Friday we got a", adjective3, noun3, ". She seems to like it when I",verb3,"because when I do she becomes",adjective33,"and eats all of my",pluralnoun3,". It is ",adjective333, "to take care of ",noun3,", mainly because they smell so much like",pluralnoun33,"and because when you scratch their", bodypart3,"they start yelling something that sounds like a", noun33,". After taking care of our new",noun3, "for a",amountoftime3, "we decided to go for a trip to",location3, "with her. While we were there our now",adjective3333, noun3, "decided that she no longer liked to", verb33, "or be with us and she ran away. We will miss her a lot.")

      print ("Thank you for doing this madlibs")
      #Allow user  to access the home page in order to play the same or other games
      mlchoiceofhomvgame = input("If you would like to do another madlibs write 'madlibs', if you would like to choose another game write 'home'.")
      if mlchoiceofhomvgame == 'madlibs' :
          madlibs()
      elif mlchoiceofhomvgame == 'home' :
          home()

    #Third mad libs, about a day at school for a person
    elif mlchoice == 'school':
      #Variables
      singularclothingarticle2 = input("singular clothing article:")
      bodypart2 = input("body part:")
      verb2 = input("verb:")
      food2 = input("food:")
      familymember2 = input("family member:")
      occupation2 = input("occupation:")
      name2 = input("name:")
      adjective2 = input("adjective:")
      adjective22 = input("adjective:")
      pluralnoun2 = input("plural noun:")
      adjective222 = input("adjective:")
      subjectmatter2 = input("subject matter:")
      adjective2222 = input("adjective:")
      noun2 = input("noun:")
      number2 = input("number:")
      pluralnoun22 = input("plural noun:")
      emotion2 = input("emotion:")
      pluralnoun222 = input("plural noun:")
      verbendingining2 = input("verb ending in -ing:")
      adjective22222 = input("adjective:")
      #Final product
      print("Every morning I wake up with my",singularclothingarticle2,"on my",bodypart2,". Then I get up and",verb2,"for about five minutes before going down stairs and eat",food2,". Then it is time for me to go to school. My",familymember2,"always drives me to school but we end up late no matter what. That is why my school day starts with a talk to the school",occupation2,"who goes by the name",name2,". ",name2,"is very",adjective2,"in the morning, and the whole thing is made even worse by the",adjective22,pluralnoun2,"that are placed by the door when I come in. After this",adjective222,"encounter I will go to my first lesson of the day. My first lesson is",subjectmatter2,"where we learn about",adjective2222,noun2,"for", number2, "hours. After that we have lunch. During lunch we eat nothing but", pluralnoun22,", my friend Billy finds them to be very",emotion2,". Then I have my last subject of the day, math. During math we count all of the",pluralnoun222,"that are",verbendingining2,". Then I go home",adjective22222,".")

      print ("Thank you for doing this madlibs")
      #Allow user  to access the home page in order to play the same or other games
      mlchoiceofhomvgame = input("If you would like to do another madlibs write 'madlibs', if you would like to choose another game write 'home'.")
      if mlchoiceofhomvgame == 'madlibs' :
          madlibs()
      elif mlchoiceofhomvgame == 'home' :
          home()

#Introducing user to the program/saying hello + welcome
print("Welcome to your game consul!")
#Getting a name to use throughout the course of the game
name = input("First please enter your name:")
print("Hi", name)
#User chooses what kind of game they want to play

def home():
    gamechoice = input("Now choose a game, do you want to play hangman or madlibs?: ")
    #Hangman game
    if gamechoice == 'hangman' or 'Hangman':
        hangman()

    #Madlibs game
    elif gamechoice == 'madlibs':
        madlibs()
home()
