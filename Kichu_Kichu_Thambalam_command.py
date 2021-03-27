import random

p_flag = "yes"
str_plots = ""
plots = 0
user_guess = 0
all_plots = []


def choose_plot():
    global str_plots, plots, all_plots
    """This function is used to choose the plot in Kichu Kichu game"""
    star_plot = random.choice(range(0, plots - 1))
    all_plots[star_plot] = '*'
    guess()
    str_plots = ' '.join(map(str, all_plots))
    print(str_plots)
    if star_plot == user_guess - 1:
        print("Yeah !!! You won  ")
    else:
        print("Oh!!! you lose my dear! don't worry try again! ")
    ask_choice()


def guess():
    global user_guess, plots
    try:
        user_guess = int(input("Guess where the star will be : "))
    except ValueError:
        print("Please guess within the sand limit and please check whether you pressed any alphabets or not!")
        guess()
    else:
        if user_guess <= 0 or user_guess > plots:
            print(f"Please guess within the limit!. The limit is from 1 to {plots}")
            guess()


def start_game():
    global str_plots, plots
    try:
        plots = int(input("Tell me how many sand parts to be included (between 5 to 13) : "))
    except ValueError:
        print("Please enter a valid number ! ")
        start_game()
    else:
        if 5 <= plots <= 13:
            for k in range(1, plots + 1):
                all_plots.append('-')
            str_plots = ' '.join(map(str, all_plots))
            print(str_plots)
            choose_plot()
        else:
            print("Sorry the limit is exceeded ! Please try again !")


def ask_choice():
    global p_flag
    try:
        p_flag = input("Do you wish to continue ? (yes or no ) :")
        if p_flag.lower() == 'y' or p_flag.lower() == "yes":
            main_game()
        elif p_flag.lower() == 'n' or p_flag.lower() == "no":
            print("You are now leaving ...! ")
        else:
            raise ValueError

    except ValueError:
        print("Please enter Yes/No or y/n. No other letters and alphabets are allowed. ")
        ask_choice()


def main_game():

    global p_flag
    while p_flag.lower() == 'y' or p_flag.lower() == 'yes':
        start_game()


main_game()
