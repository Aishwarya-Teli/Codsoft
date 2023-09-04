import random
option=["Rock","Paper","Scissors"]
user_ch=input("ckoose Rock,Paper or Scissors:")
computer_ch=random.choice(option)
print("user choose:",user_ch)
print("computer choose:",computer_ch)
if(user_ch==computer_ch):
    print("it is a tie")
elif(user_ch=="Rock"and computer_ch=="Paper"):
    print("you loose,computer select peper")
elif(user_ch=="Rock"and computer_ch=="Scissor"):
    print("you win ,computer select scissor")
elif(user_ch=="Paper"and computer_ch=="Scissor"):
    print("you loose , computer select scissor")
elif(user_ch=="Paper"and computer_ch=="Rock"):
    print("you win ,computer select rock")
elif(user_ch=="Scissor"and computer_ch=="Rock"):
    print("you loose ,computer select rock")
elif(user_ch=="Scissor"and computer_ch=="Paper"):
    print("you win,computer select paper")
    
else:
    print("invalid:choose any one")
