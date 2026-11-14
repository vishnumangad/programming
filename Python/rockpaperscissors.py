import random
rock=('''    
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
paper=('''   
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
scissors=('''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
 ''')
game=[rock,paper,scissors]
ROCK=game[0]
PAPER=game[1]
SCISSORS=game[2]
user=input("What do you choose? Rock, Paper or Scissors?").upper()
if(user=="ROCK"):
    print("Your Choice: \n",ROCK)
elif(user=="SCISSORS"):
    print("Your Choice: \n",SCISSORS)
elif(user=="PAPER"):
    print("Your Choice: \n",PAPER)
else:
    print("Invalid choice!")
comp=random.choice(game)
print("Computer chose: \n",comp)
if(user=="ROCK" and comp==SCISSORS):
    print("You Win!")
elif(user=="PAPER" and comp==ROCK):
    print("You Win!")
elif(user=="SCISSORS" and comp==PAPER):
    print("You Win!")
else:
    print("Computer Wins! Better luck next time.")

