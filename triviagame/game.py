from random import randrange

MAX_PLAYERS = 6
WINNING_SCORE = 10


class Game:
    def __init__(self):
        self.players = []
        self.places = [0] * MAX_PLAYERS
        self.purses = [0] * MAX_PLAYERS
        self.in_detention = [0] * MAX_PLAYERS

        self.pop_culture_questions = []
        self.science_questions = []
        self.witchcraft_questions = []
        self.fashion_questions = []

        self.current_player = 0
        self.is_getting_out_of_detention = False

        for i in range(50):
            self.pop_culture_questions.append(f"Pop Culture Question {i}")
            self.science_questions.append(f"Science Question {i}")
            self.witchcraft_questions.append(f"Witchcraft Question {i}")
            self.fashion_questions.append(self.create_fashion_question(i))

    @staticmethod
    def create_fashion_question(index):
        return f"Fashion Question {index}"

    def is_playable(self):
        return self.how_many_players >= 2

    def add(self, player):
        self.players.append(player)
        self.places[self.how_many_players] = 0
        self.purses[self.how_many_players] = 0
        self.in_detention[self.how_many_players] = False

        print(f"{player.name} was added. They are player number {len(self.players)}")

        return True

    @property
    def how_many_players(self):
        return len(self.players)

    @staticmethod
    def roll_dice():
        return randrange(5) + 1

    def player_turn(self):
        roll = self.roll_dice()
        print(f"{self.players[self.current_player]} is the current player")
        print(f"They have rolled a {roll}")

        if self.in_detention[self.current_player]:
            if roll % 2 != 0:
                self.is_getting_out_of_detention = True

                print(f"{self.players[self.current_player]} is getting out of detention")
                self.places[self.current_player] = self.places[self.current_player] + roll
                if self.places[self.current_player] > 11:
                    self.places[self.current_player] = self.places[self.current_player] - 12

                print(f"{self.players[self.current_player]}'s new location "
                      f"is {str(self.places[self.current_player])}")
                print(f"The category is {self.current_category}")
                self._ask_question()
            else:
                print(f"{self.players[self.current_player]} is not getting out of detention")
                self.is_getting_out_of_detention = False
        else:
            self.places[self.current_player] = self.places[self.current_player] + roll
            if self.places[self.current_player] > 11:
                self.places[self.current_player] = self.places[self.current_player] - 12

            print(f"{self.players[self.current_player]}'s new location "
                  f"is {str(self.places[self.current_player])}")
            print(f"The category is {self.current_category}")
            self._ask_question()

    def can_player_answer_q(self):
        current_player = self.players[self.current_player]
        if self.current_category == 'Pop Culture':
            skill_level = current_player.pop_culture_skill_level
        elif self.current_category == 'Science':
            skill_level = current_player.science_skill_level
        elif self.current_category == 'Witchcraft':
            skill_level = current_player.witchcraft_skill_level
        else:
            skill_level = current_player.fashion_skill_level

        if randrange(9) < skill_level:
            return True
        else:
            return False

    def _ask_question(self):
        if self.current_category == 'Pop Culture':
            print(self.pop_culture_questions.pop(0))
        if self.current_category == 'Science':
            print(self.science_questions.pop(0))
        if self.current_category == 'Witchcraft':
            print(self.witchcraft_questions.pop(0))
        if self.current_category == 'Fashion':
            print(self.fashion_questions.pop(0))

    @property
    def current_category(self):
        if self.places[self.current_player] in [0, 4, 8]:
            return 'Pop Culture'
        if self.places[self.current_player] in [1, 5, 9]:
            return 'Science'
        if self.places[self.current_player] in [2, 6, 10]:
            return 'Witchcraft'
        return 'Fashion'

    def was_correctly_answered(self):
        if self.in_detention[self.current_player]:
            if self.is_getting_out_of_detention:
                print('Answer was correct!!!!')
                self.purses[self.current_player] += 1
                print(f"{self.players[self.current_player]} now "
                      f"has {self.purses[self.current_player]} Gold Coins.")

                winner = self._did_player_win()
                self.current_player += 1
                if self.current_player == len(self.players):
                    self.current_player = 0

                return winner
            else:
                self.current_player += 1
                if self.current_player == len(self.players):
                    self.current_player = 0
                return True
        else:
            print("Answer was correct!!!!")
            self.purses[self.current_player] += 1
            print(f"{self.players[self.current_player]} now "
                  f"has {self.purses[self.current_player]} Gold Coins.")

            winner = self._did_player_win()
            self.current_player += 1
            if self.current_player == len(self.players):
                self.current_player = 0

            return winner

    def wrong_answer(self):
        print("Question was incorrectly answered")
        print(f"{self.players[self.current_player]} was sent to detention")
        self.in_detention[self.current_player] = True

        self.current_player += 1
        if self.current_player == len(self.players):
            self.current_player = 0
        return True

    def _did_player_win(self):
        return not (self.purses[self.current_player] == WINNING_SCORE)
