# Collecting the user name to address the user in the program later.
username = input("Enter your name : ")

print(f"Hi {username}! Welcome to the movie collection app.")

# Movies list is to hold all movies.
movies = []

# Display the specific movie information
def display_movie(movie):
    print(f"\n Movie Name {movie['movie_name']}"
          f"\n Director Name {movie['director_name']}"
          f"\n Released Year {movie['release_year']}")

# Add the movie details from the user
def add_movies():
    movie = input("Enter the movie name: ")
    director = input("Enter the director name: ")
    year = input("Enter the released year: ")
    movie = {
        "movie_name" : movie,
        "director_name" : director,
        "release_year" : year
    }
    movies.append(movie)


# Display all the movies one by one
def display():
    for movie in movies:
        display_movie(movie)


# Display the movie information while the movie title is given
def find():
    movie = input("Enter the movie name to find : ")
    movie_details = {}
    for i in movies:
        if i["movie_name"] == movie:
            movie_details = i
    if movie_details:
        print("Yay!! The movie is available!")
        display_movie(movie_details)
    else:
        print("Ouch! The movie is not found")


# Terminating the program
def terminate():
    print("Thanks for using the app! The program is getting terminated.")

# Dictionary to hold the choices and functions
operations = {
    'a': add_movies,
    's': display,
    'f': find,
    'q': terminate
}


menu = """a to add Movie
s to show all movies
f to find a specific movie details
q to quit the app"""

print("Please select an operation by typing the letter as mentioned in the below description.\n",menu)
choice = ''


# Actual program begins
while choice!='q':
    choice = input("your choice : ")
    if choice in operations:
        selected_action = operations[choice]
        selected_action()
    else:
        print("Oh bad! This command is not in my tasks list. Can you please try again? ")
        print(menu)
