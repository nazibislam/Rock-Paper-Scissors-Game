##Rock, paper, scissors game
import random
print("Welcome to Rock, papers and scissors game: ")
user=int(input("Press 0 for rock, 1 for paper and 2 for scissors: "))

rock= '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper= '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissor='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
computer=random.randint(0,2)
if user>=3 or user<0:
    print("Invalid")
elif user==0:
    print(f"You chose Rock\n{rock}")
    if computer==0:
        print(f"Computer chose rock.\n{rock}\nIt's a draw")
    elif computer==1:
        print(f"Computer chose papers.\n{paper}\nYou lose")
    else:
        print(f"Computer chose scissors.\n{scissor}\nYou win")

elif user==1:
    print(f"You chose Paper\n{paper}")
    if computer==0:
        print(f"Computer chose rock.\n{rock}\nYou win")
    elif computer==1:
        print(f"Computer chose papers.\n{paper}\nIt's a draw")
    else:
        print(f"Computer chose scissors.\n{scissor}\nYou lose")
        
elif user==2:
    print(f"You chose Scisoor\n{scissor}")
    if computer==0:
        print(f"Computer chose rock.\n{rock}\nYou lose")
    elif computer==1:
        print(f"Computer chose papers.\n{paper}\nYou win")
    else:
        print(f"Computer chose scissors.\n{scissor}\nIt's a draw")
        
    
