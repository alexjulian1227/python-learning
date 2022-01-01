import turtle
import pandas

data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
game_is_on = True
all_states = data.state.to_list()
answer_title = "Guess the state"
guessed_states = []
needed_guess = 50
while game_is_on:
    answer_state = screen.textinput(title=answer_title, prompt="Enter another state name.").title()
    # if answer_state == "Exit":
    #     missing_states = []
    #     for state in all_states:
    #         if state not in guessed_states:
    #             missing_states.append(state)
    #     new_data = pandas.DataFrame(missing_states)
    #     new_data.to_csv("states_to_learn.csv")
    #
    #     break
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        a = data['state'] == answer_state
        a = data[a]
        state_x = int(a.x)
        state_y = int(a.y)
        show_state = turtle.Turtle()
        show_state.hideturtle()
        show_state.pu()
        show_state.goto(state_x, state_y)
        show_state.write(answer_state, font=("Courier", 10, "normal"), align="center")
        guessed_states.append(answer_state)
        correct_guess = (len(guessed_states))
        answer_title = f"{len(guessed_states)}/{needed_guess} States Correct"
    else:
        pass
    # getting the coordinate of the screen in turtle graphics
    # def get_mouse_click_coor(x, y):
    #     print(x, y)
    #
    # turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
#states_to_learn.csv

