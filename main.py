import turtle
from score import ScoreBoard
from game import Game
import time

image = "blank_states_img.gif"
game = Game()
score_board = ScoreBoard()


screen = turtle.Screen()
screen.addshape(image)
screen.title("U.S. States Game")
turtle.shape(image)


game_is_on = True

while game_is_on:
    answer = screen.textinput(title=str(score_board.score) + "/" + str(len(game.csv_data)) + " completed",
                              prompt="What is another US State name?")
    if answer:
        if game.is_valid_state(answer):
            score_board.score += 1
        game_is_on = game.has_more_states()
    else:
        score_board.print_score(len(game.csv_data))
        game_is_on = False

screen.exitonclick()








