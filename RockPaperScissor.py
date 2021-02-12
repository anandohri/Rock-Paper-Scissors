import random
import string


possible_hands = ['rock', 'paper', 'scissors']


class RockPaperScissor:
    def __init__(self):
        self.my_hand = ''
        self.sys_hand = ''
        self.sys_score = 0
        self.my_score = 0

    def generate_sys_hand(self):
        self.sys_hand = random.choice(possible_hands)

    def validate_my_hand(self):
        if string.lower(self.my_hand) in ['rock', 'paper', 'scissors']:
            print('Valid Choice')
        else:
            print('Invalid Choice')
            raise Exception

    def results(self):
        wanna_play = 'y'
        try:
            while string.lower(wanna_play) == 'y':
                self.my_hand = raw_input('Choose([rock, paper, scissors]): ')
                self.validate_my_hand()

                self.generate_sys_hand()
                print('System Choice: ' + self.sys_hand)

                if string.lower(self.my_hand) == self.sys_hand:
                    print('Draw')
                elif (string.lower(self.my_hand) == 'rock' and self.sys_hand == 'scissors') or \
                        (string.lower(self.my_hand) == 'paper' and self.sys_hand == 'rock') or \
                        (string.lower(self.my_hand) == 'scissors' and self.sys_hand == 'paper'):
                    print('You win')
                    self.score_keeping('me')
                else:
                    print('You loose')
                    self.score_keeping('sys')

                wanna_play = raw_input('Wanna play again(y/n): ')

            if string.lower(wanna_play) != 'y':
                print('#####=====Final Scores=====#####')
                print('   System      |      Player')
                print('     ' + str(self.sys_score) + '         |         ' + str(self.my_score))

        except Exception as e:
            print(e)

    def score_keeping(self, winner):
        if winner == 'sys':
            self.sys_score += 1
        elif winner == 'me':
            self.my_score += 1


x = RockPaperScissor()
x.results()
