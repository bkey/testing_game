from triviagame.game import Game
from triviagame.player import Player


if __name__ == '__main__':
    no_winner_yet = True

    game = Game()

    buffy = Player("Buffy", fashion_skill_level=10)
    willow = Player("Willow", science_skill_level=10, witchcraft_skill_level=10)
    xander = Player("Xander", pop_culture_skill_level=10)
    cordy = Player("Cordelia", pop_culture_skill_level=8, fashion_skill_level=10)

    game.add(buffy)
    game.add(willow)
    game.add(xander)
    game.add(cordy)

    while True:
        current_player = game.current_player
        game.player_turn()

        can_answer_question = game.can_player_answer_q()
        if can_answer_question:
            no_winner_yet = game.was_correctly_answered()
        else:
            no_winner_yet = game.wrong_answer()

        if not no_winner_yet:
            print(f"{game.players[current_player]} Wins!")
            break
