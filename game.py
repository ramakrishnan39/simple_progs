import random as r
rock = '''
    _______
---'   ____)
      (___)__)
      (___)__)
      (__)__)
---.__(__)_)
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
          /______)
       ___\_______)
      (____)
---.__(___)
'''
user_input=int(input("What do you choose ? (0 - rock, 1 - paper, 2 - scissors) :"))
game_list=[rock,paper,scissors]
v_names=["rock","paper","scissors"]
print(v_names[user_input] + " " + game_list[user_input])
print("Computer's choice")
comp_input=r.randint(0,2)
print(v_names[comp_input] + " " + game_list[comp_input])
if user_input==comp_input:
  print("Match ended in Draw")
elif (user_input,comp_input) in [(0,1),(1,2),(2,0)]:
  print("You lost!! :( Try again buddy for your luck.")
else:
  print("Hurray ! You won the game!")
