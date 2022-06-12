import random
R="rock"
P="paper"
S="scissors"
options=(R,P,S)

while True:
    player_input=input("Type Rock,Paper or Scissors to play.").lower()
    if player_input not in options:
        print("Please enter a valid option")
        continue
    computer_select=random.choice([R,P,S])
    print('Player', player_input, ':' 'Computer', computer_select, '.')

    if player_input==R and computer_select==S:
        print('YOU WON!')
    elif player_input ==P and computer_select==R:
            print("YOU WON!")
    elif player_input ==S and computer_select==P:
            print("YOU WON!")
    elif player_input==computer_select:
        print("it's draw. Try again")
        continue
    else:
        print('Computer won!')
    break
print('Goodbye!')

