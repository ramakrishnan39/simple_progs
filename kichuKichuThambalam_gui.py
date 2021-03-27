import random
import tkinter as tk

BG_COLOR = "#ffc93c"
m = tk.Tk()
m.title("Kichu Kichu Thambalam")
m.geometry('640x480')
m.config(bg=BG_COLOR)

all_plots = []
str_plots = ""

l1 = tk.Label(text="Tell me the number of Sand plots (should be 5 to 13) ", bg = BG_COLOR)
t1 = tk.Entry()
l2 = tk.Label(text="Guess where the star will be ", bg = BG_COLOR)
l3 = tk.Label(bg = BG_COLOR)
l4 = tk.Label(bg = BG_COLOR)
l5 = tk.Label(bg = BG_COLOR)
t2 = tk.Entry(bg = BG_COLOR)

msg = tk.Message()
p_flag = "y"
choice = tk.StringVar()


def set_yes():
    global p_flag
    p_flag = "yes"


def set_no():
    global p_flag
    p_flag = "no"


def set_plots(pn_plots):
    global all_plots, str_plots
    str_plots = ""
    for k in range(1, pn_plots + 1):
        all_plots.append('^')
    str_plots = ' '.join(map(str, all_plots))


def see():
    global all_plots, str_plots
    plots = t1.get() if t1.get() else l3.config(text="Please enter any value")
    n_plots = int(plots)
    if 5 <= n_plots <= 13:
        set_plots(n_plots)
        l3.config(text=str_plots)
        l2.grid(row=4, column=0)
        t2.grid(row=3, column=1)
        btn2.grid(row=4, column=1)
    else:
        l3.config(text="Sorry ! Please tell me your choice as between 5 to 13 !")


def choose_plot():
    """This function is used to play the game"""
    global all_plots, str_plots
    plots = t1.get() if t1.get() else l3.config(text="Please enter any value")
    """This function is used to choose the plot in Kichu Kichu game"""
    set_plots(int(plots))
    star_plot = random.choice(range(0, len(str_plots) - 1))
    all_plots[star_plot] = '*'
    user_guess = int(t2.get()) if t2.get() else l3.config(text="Enter a valid choice!")
    str_plots = ' '.join(map(str, all_plots))
    l3.config(text=str_plots)
    if star_plot == user_guess - 1:
        l4.config(text="Yeah !!! You won  ")
    else:
        l4.config(text="Oh you lose my dear! don't worry try again! ")
    l4.grid(row=3, column=0)


def play():
    global msg, all_plots, str_plots, p_flag
    p_flag = 'yes'
    while p_flag.lower() == 'y' or p_flag.lower() == 'yes':
        all_plots = []
        str_plots = ""
        choose_plot()
        l5.config(text="Do you wish to continue ? ")
        l5.grid(row=4, column=0)
        btn3.grid(row=5, column=1)
        btn4.grid(row=6, column=1)
    else:
        l3.config(text="You selected No")


def reset_game():
    l3.grid_forget()
    l4.grid_forget()
    l2.grid_forget()
    t2.grid_forget()
    l5.grid_forget()
    btn2.grid_forget()
    btn3.grid_forget()
    btn4.grid_forget()


btn1 = tk.Button(text="See sand clouds ", command=see)
btn2 = tk.Button(text="Guess", command=play)
btn3 = tk.Button(text="Yes", command=reset_game)
btn4 = tk.Button(text="No", command=exit)
l1.grid(row=0, column=0)
t1.grid(row=0, column=1)
btn1.grid(row=1, column=0)
l3.grid(row=2, column=0)

m.mainloop()
