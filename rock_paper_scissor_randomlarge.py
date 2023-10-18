import random
roll = random.randint(1,3)
if  roll == 1:
    computer_choice = 'scissor'
if  roll == 2:
    computer_choice = 'rock'
if  roll == 3:
    computer_choice = 'paper'
user_choice = input('Do you want rock, paper or scissors? \n')
if computer_choice ==  user_choice:
    print('TIE' + computer_choice)
elif user_choice == 'rock' and computer_choice == 'scissor':
    print('You WIN computer was: ' + computer_choice)
elif user_choice == 'paper' and computer_choice == 'rock':
    print('You WIN computer was: ' + computer_choice)
elif user_choice == 'scissor' and computer_choice == 'paper':
    print('You WIN computer was: ' + computer_choice)
else:
    print("You loose, computer was: " + computer_choice)