import turtle
import pandas as pd
import csv
screen = turtle.Screen()
screen.setup(800, 600)

screen.bgcolor("black")
screen.update
screen.title("INDIAN STATE GUESS")
image = "C:\\Users\\PRATHAM\\Downloads\\image.gif.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("C:\\Users\\PRATHAM\\Downloads\\Indian_States_UTs_List_with_coordinates.csv")
all_states = df["State/UT"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                    prompt="whats another state??").title()
 
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        state_data = df[df["State/UT"] == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

    if answer_state.lower() == "exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
                print(missing_states)
            new_data = pd.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
        break
 

