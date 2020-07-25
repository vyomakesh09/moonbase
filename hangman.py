
#!/usr/bin/env python3

import random

'''def asking_word(current_teams_asking, vowels):
    while '-' in current_teams_asking or ' ' in current_teams_asking:
        asking_word = current_teams_asking
    
    return asking_word'''

# Getting all the players, dividing into two teams
def hangman(player1, player2, player3, player4):
    team_1 = random.choices([player1, player2, player3, player4], k=2)
    team_2 = random.choices([player1, player2, player3, player4], k=2)
    
    vowels = ['a', 'e', 'i', 'o', 'u']

    #current_team = random.choice([team_1, team_2])
    current_team = team_1 
    another_team = team_2
    while current_team != another_team:
        current_teams_asking = input("Whats your word?\n")
        asking_word_list = [letter if letter in vowels else '_' for letter in current_teams_asking]
        asking_word = ''.join(asking_word_list)
        print(asking_word)

        anothers_team_answer = input("Guess your letter!\n")
        answer_word_list = [letter if letter in current_teams_asking else '_' for letter in anothers_team_answer]
        # = ''.join(answer_word_list)
        print(answer_word_list)
            


 
hangman('gin', 'shinsu', 'hara', 'krik')
