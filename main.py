import turtle
import pandas

data = pandas.read_csv("50_states.csv")
# Converting the pandas dataframe into a list
all_states = data.state.to_list()

# Keep track of the score
guessed_states = []

screen = turtle.Screen()
screen.title("US States Game")
screen.setup(height=491, width=725)

# Setting the background (turtle) as the US picture
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Use a loop to allow the user to keep guessing
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state's name?").title()

    # Exits the game if exit is typed as well as creates a csv with all missing states
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    # check if the guess is among the 50 states
    elif answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        
        # Write correct guesses onto the map
        t.write(answer_state)
        


screen.exitonclick()



