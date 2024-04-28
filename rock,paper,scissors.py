import random
#----------------------------------------
player_name=input("What's your name? ").capitalize()
computer_name=input("What do you want to call the Computer? ").capitalize()
#----------------------------------------
while True:
 choices= ["rock","paper","scissors"]
 player= None
 computer= random.choice(choices)

 while player not in choices:
  player= input("Rock, Paper or Scissors?: ").lower()

 if player==computer:
  print(computer_name+": "+ computer)
  print(player_name+": "+ player)
  print("Tie!")
#----------------------------------------
 elif player=="rock":
 
  if computer=="paper":
   print(computer_name+": "+ computer)
   print(player_name+": "+ player)
   print("You Loose!")
  
  if computer=="scissors":
   print(computer_name+": "+ computer)
   print(player_name+": "+ player)
   print("You Win!")
#----------------------------------------
 elif player=="scissors":
 
  if computer=="rock":
   print(computer_name+": "+ computer)
   print(player_name+": "+ player)
   print("You Loose!")
  
  if computer=="paper":
   print(computer_name+": "+ computer)
   print(player_name+": "+ player)
   print("You Win!")
#----------------------------------------
 elif player=="paper":
 
  if computer=="scissors":
   print(computer_name+": "+ computer)
   print(player_name+": "+ player)
   print("You Loose!")
  
  if computer=="rock":
   print(computer_name+": "+ computer)
   print(player_name+": "+ player)
   print("You Win!")
 #----------------------------------------  
 play_again=input("Play again? (y/n): ").lower()
 
 if play_again != "y":
  break
 #----------------------------------------
print("Bye!")