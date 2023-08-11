from turtle import Screen, Turtle, shape
import pandas

screen = Screen()
screen.setup(725, 491)
screen.title("Guess the State")
image = "blank_states_img.gif"
screen.addshape(image)
shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
answer = ""
guessed_states = []

while len(guessed_states) != len(all_states):
    answer = screen.textinput(
        title=f"{len(guessed_states)}/{len(all_states)} Guess a state",
        prompt="What other state do you know?"
    ).title()
    if answer.lower() == "exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missed_states")
        break
    if answer in all_states:
        state_data = data[data.state == answer]
        timmy = Turtle()
        timmy.hideturtle()
        timmy.penup()
        timmy.goto(int(state_data.x), int(state_data.y))
        timmy.write(answer)
        guessed_states.append(answer)

screen.exitonclick()