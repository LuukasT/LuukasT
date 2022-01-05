def add_new_movie_and_rating(dictionary, movie, rating):
    if movie in dictionary:
        return False
    else:
        dictionary[movie] = rating
        return True


def change_rating(dictionary, movie, rating):
    if movie not in dictionary:
        return False
    else:
        dictionary[movie] = rating
        return True


def print_all_movies(dictionary):
    dictionary1 = sorted(dictionary)
    for movie in dictionary1:
        print("{:s} {:d}".format(movie, dictionary[movie]))


def find_movies_with_rating(dictionary, rating):
    dictionary_movies = []
    for i in dictionary:
        if rating == dictionary[i]:
            dictionary_movies.append(i)

    return dictionary_movies

def ask_user_input():
    print("Choose 1-5.")
    print("1: Add a new movie and rating.")
    print("2: Change the rating of the movie.")
    print("3: Print all movies and their ratings.")
    print("4: Find all movies with a specific rating.")
    print("5: Exit.")
    user_input = int(input())
    print("")

    return user_input

    
def main():
    print("Welcome to the database of the movie ratings.\n")
    dictionary = {}

    user_input = ask_user_input()
    while user_input != 5:
        if user_input == 1:
            movie = input("Enter the movie.\n")
            rating = int(input("Enter the rating(4-10).\n"))
            ok = add_new_movie_and_rating(dictionary, movie, rating)
            if ok == True:
                print(movie, "has been added into the database,")
            else:
                print(movie, "is already in the database. Choose 2 if you want to change the rating of the movie.")
            print("")
            user_input = ask_user_input()
        elif user_input == 2:
            movie = input("Enter the movie.\n")
            rating = int(input("Enter the new rating(4-10).\n"))
            ok = change_rating(dictionary, movie, rating)
            if ok == True:
                print("The rating of", movie, "has been changed.")
            else:
                print(movie, "is not in the database. Choose 1 if you want to add the movie.")
            print("")
            user_input = ask_user_input()
        elif user_input == 3:
            print("The movies in the database:")
            print_all_movies(dictionary)
            print("")
            user_input = ask_user_input()
        elif user_input == 4:
            rating = int(input("Enter the rating.\n"))
            dictionary_movies = find_movies_with_rating(dictionary, rating)
            if len(dictionary_movies) == 0:
                print("There are no movies with rating", rating, "in the database.")
            else:
                for movie in dictionary_movies:
                    print(movie)
            print("")
            user_input = ask_user_input()
        else:
            print("You chose an invalid number.\n")
            user_input = ask_user_input()

main()