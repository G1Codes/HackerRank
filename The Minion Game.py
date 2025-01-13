
'''
*The Minion Game*

Kevin and Stuart want to play the ‘The Minion Game’.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String S = BANANA
Kevin’s vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

Your task is to determine the winner of the game and their score.

'''

def minion_game(string):
    Kevin=Stuart=0
    vowels= 'AEIOU'
    
    for i in range(len(string)):
        if string[i] not in vowels:
            Stuart+=len(string)-i
        else:
            Kevin+=len(string)-i
    if Kevin>Stuart:
        print(f"Kevin {Kevin}")
    elif Kevin<Stuart:
        print(f"Stuart {Stuart}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)