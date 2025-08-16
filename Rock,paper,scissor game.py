 # Rock,paper,scissor game
import random
user_choice=int(input("Enter the number corresponding to your choice:\n0.Rock\n1.Paper\n2.Scissors\n"))
if user_choice < 0 or user_choice > 2:
    print("Invalid choice, please try again.")
    exit()
else:    
  computer_choice=random.randint(0,2)
  print("Computer chose:", computer_choice)
  if user_choice == computer_choice:
    print("It's a tie!")
  elif (user_choice == 0) and (computer_choice == 2):
    print("You win! Rock crushes Scissors.")
  elif (user_choice==2) and (computer_choice ==0):
    print("You lose! Rock crushes Scissors.")  
  elif user_choice> computer_choice:
    print("You win!") 
  elif computer_choice > user_choice:
    print("You lose!")     
  
print("Thanks for playing!")
