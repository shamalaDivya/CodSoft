import random
print('welcome to rock paper scissor game')
print('----------------------------------')
while(True):
    print('enter r for rock,s for scissor,p for paper')
    you=input('enter the choice ')
    if (you=='r' or you=='p' or you=='s'):
        computer=random.choice(['r','p','s'])

        if you==computer:
            print(f'Its tie! because you and computer choose {computer}')
        elif (you=='r' and computer=='s') or (you=='p' and computer=='r') or (you=='s' and computer=='p' ):
            print(f'you won! because you choose {you} and computer choose {computer} ')
        else:
            print(f'you lose! because you choose {you} and computer choose {computer}')
        choice=input('Do you want to play again(yes/no) ') .lower()
        if choice!='yes':
            break
    else:
        print('Invalid choice! please enter valid choice')
print('thanks for playing')