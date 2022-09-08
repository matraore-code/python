import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
map = [rock, paper, scissors]
computer = random.randint(0, 2)
result = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if result < 0 and result > 2
    print("you lose! invalid number")
if result == 0:
  print(map[result])
  print(f"Computer choose \n{map[computer]}")
  if result == computer:
    print("you draw")
  elif computer == 1 :
    print("you loose.")
  elif computer == 2 :
    print("you win.")
elif result == 1:
  print(map[result])
  print(f"Computer choose \n{map[computer]}")
  if result == computer:
    print("you draw")
  elif computer == 0 :
    print("you loose.")
  elif computer == 2 :
    print("you win.")
else :
  print(map[result])
  print(f"Computer choose \n{map[computer]}")
  if result == computer:
    print("you draw")
  elif computer == 0 :
    print("you loose")
  elif computer == 1 :
    print("you win")


  
