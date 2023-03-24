from turtle import Turtle
import pandas as pd

SOURCE = "50_states.csv"


class Game(Turtle):

    def __init__(self):
        super().__init__()
        self.csv_data = pd.read_csv(SOURCE)
        self.remain = self.csv_data.state.tolist()
        self.hideturtle()
        self.penup()

        print(f"Loaded with {len(self.remain)} states of type {type(self.remain)}")
        print(f"Loaded values {self.remain}")

    def has_more_states(self):
        return len(self.csv_data) > 0

    def is_valid_state(self, state_name):
        state = self.csv_data[self.csv_data.state.str.lower() == state_name.lower()]
        if len(state) > 0 and state.state.item() in self.remain:
            item_state_name, item_state_x, item_state_y = state.state.item(), state.x.item(), state.y.item()
            print(f"You guessed it right : {item_state_name}")
            self.goto(item_state_x, item_state_y)
            self.write(item_state_name)
            self.remain.remove(item_state_name)
            return True
        return False

