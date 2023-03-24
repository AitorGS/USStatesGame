from turtle import Turtle
import time

FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.start_time = time.time()
        self.goto(-400, 340)

        self.score = 0

    def print_score(self, total_answers):
        self.clear()
        elapsed_time = (time.time() - self.start_time) / 1000.0

        if self.score == total_answers:
            self.write(f"You have won! Elapsed time: {elapsed_time:.2f} seconds", font=FONT)
        else:
            self.write(f"Game over! You have achieved {self.score}/{total_answers}  correct answers", font=FONT)

