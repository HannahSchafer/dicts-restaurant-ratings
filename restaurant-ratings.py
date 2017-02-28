import sys
import random


def make_restaurant_dict(filename):
    """Creates restaurant:rating dictionary.
    """

    text = open(filename)
    restaurant_ratings = {}

    # Iterates through text, splits lines into restaurant and rating.
    # Adds the data to the restaurant_ratings dictionary.
    for line in text:
        restaurant, rating = line.rstrip().split(":")
        restaurant_ratings[restaurant] = int(rating)

    return restaurant_ratings


def get_rating(filename):
    """Adds restaurant rating to the dictionary from user input
    and prints all restaurants and ratings in a nice format.
    """
    # Creates dictionary from file
    restaurant_ratings = make_restaurant_dict(filename)

    while True:
        print "Enter 'view' to see all ratings."
        print "Enter 'add' to add rating."
        print "Enter 'update random' to update a random restaurant rating."
        print "Enter 'update restaurant' to update a specific restaurant rating."
        print "Enter 'quit' to exit."

        user_choice = raw_input("> ")
        user_choice = user_choice.lower()

        if user_choice == 'view':

            sorted_restaurants = sorted(restaurant_ratings.items())

            # Prints and rating in a readable format.
            for restaurant, rating in sorted_restaurants:
                print "{} is rated at {}.".format(restaurant, rating)

        elif user_choice == 'add':

            user_restaurant = raw_input("Please enter a restaurant name: ")
            user_rating = raw_input("Please enter this restaurant's rating: ")
            # Adding user input to dictionary
            restaurant_ratings[user_restaurant] = int(user_rating)

        elif user_choice == 'update random':
            random_restaurant = random.choice(restaurant_ratings.keys())
            print "{} has a rating of {}.".format(
                random_restaurant, restaurant_ratings[random_restaurant])

            new_rating = raw_input("What should the new rating be? ")
            restaurant_ratings[random_restaurant] = int(new_rating)

        elif user_choice == 'update restaurant':
            user_restaurant = raw_input("Which restaurant would you like to update?")
            user_rating = raw_input("What rating would you like to give the restaurant?")

            restaurant_ratings[user_restaurant] = int(user_rating)

        else:
            break

get_rating(sys.argv[1])
