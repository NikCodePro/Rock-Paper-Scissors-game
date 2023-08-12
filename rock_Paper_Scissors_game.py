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
---'   ____)________
          __________)
          _________)
         _________)
---.____________)
'''

scissors = '''
    _______
---'   ____)_____
          _______)
       ___________)
      (____)
---.__(___)
'''

# print(scissors)


input_by_user = int(input("Welcome to rock, paper & scissors game ! Type 1 for rock , 2 for paper & 3 for scissors -->" ))

comp = random.randint(1, 3)

# print(comp)

if comp == 1:
    print(rock)
elif comp == 2:
    print(paper)
elif comp == 3:
    print(scissors)

if input_by_user == 1 and comp == 3:
    print("You Won the Game")
elif input_by_user == 2 and comp == 1:
    print("You Won the Game")
elif input_by_user == 3 and comp == 2:
    print("You Won the Game")
elif input_by_user == comp:
    print("match draw !!!!")
else:
    print("You Lose the Game")