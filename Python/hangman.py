import random
print("Welcome to Hangman!")
print("""                                      
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/ """)
print("""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
        ===""")
hang = [
    """
     +---+
     |   |
     O   |
    /|\  |
    / \  |
        ===""",
    """
     +---+
     |   |
     O   |
    /|\  |
    /    |
        ===""",
         """
      +---+
      |   |
      O   |
     /|\  |
          |
         ===""",
            
    """
     +---+
     |   |
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     |   |
     O   |
     |   |
         |
        ===""",
    """
     +---+
     |   |
     O   |
         |
         |
        ===""",
    """
    +---+
    |   |
        |
        |
        |
       ==="""
    ]


words=['Cat', 'Dog', 'Elephant', 'Giraffe', 'Lion', 'Tiger', 'Zebra', 'Monkey', 'Kangaroo', 'Panda']
correct=[]
word=random.choice(words).lower()
print(word)
placeholder="_"*len(word)
print(placeholder)
gameover=False
lives=6
while(not gameover):
    display=""
    guess=input("Guess a letter: ").lower()
    for i in word:
      if(guess==i):
        display += guess
        correct.append(guess)
      elif(i in correct):
          display+=i
      else:
        display += "_"
    print(display)
    if(guess not in word):
        lives-=1
        print("You guessed wrong, you lose a life, your remaining lives are", lives)
    if(guess in word):
        print("You already guessed this letter!")
        if(lives==0):
            gameover=True
            print("**********You lost!**********")
    if("_" not in display):
        gameover=True
        print("**********You won!**********")
    print(hang[lives])
