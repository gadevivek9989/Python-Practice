import random
print("the game is ROCK,PAPPER,SCISSORS")
print()
print("you have some game rules\n1->ROCK\n2->PAPPER\n3->SCISSOR")
print()
print("ROCK VS PAPER -> ROCK WINS")
print("ROCK VS SCISSOR -> SCISSOR WINS")
print("PAPER VS SCISSOR -> SCISSOR WINS ")
while True:
   player = int(input("enter any option to select ROCK,PAPER,SCISSOR"))
    

   if (player == 1):
      print("You selected ROCK and now computers chance\n")
      player_choice = 'ROCK'
   elif (player == 2):
      print("You selected PAPPER and now computers chance\n")
      player_choice = 'PAPER'
   elif (player == 3):
      print("You selected SCISSOR and now computers chance\n")
      player_choice = 'SCISSOR'

   print(f"you now selected {player_choice}")
        

   computer = random.randint(1, 3)

   if (computer == 1):
      print("computer selected ROCK")
      computer_choice = 'ROCK'
   elif (computer == 2):
      print("computer selected PAPPER \n")
      computer_choice = 'PAPPER'
   else:
      print("computer selected SCISSOR \n")
      computer_choice = 'SCISSOR'
   print()
   print()
   print(f"coputer selected {computer_choice}")

   print("---------------------------------------------------------------------------------------")
   print(player_choice + "vs" + computer_choice)

   

   if (player == 1 and computer == 2) or (computer == 2 and player == 1):
      result = 'ROCK'
   elif (player == 2 and computer == 3) or (player == 3 and computer == 2):
      result = 'SCISSOR'
   elif (player == 1 and computer == 3) or (computer == 1 and player == 3):
      result = 'Rock'

   if (result == "DRAW"):
      print("Its a tieee.......")
   elif (result == player_choice):
      print("you won.......")
   elif(result == computer_choice):
      print("you lose........")

   print("do you want to play again y/n")
   ans = input().lower
   if ans == 'y':
      break
    




