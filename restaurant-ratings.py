import sys


def make_restaurant_dict(filename):
    """Prints restaurant ratings.
    """

    text = open(filename)
    restaurant_ratings = {}

    # Iterates through text, splits lines into restaurant and rating.
    # Adds the data to the restaurant_ratings dictionary.
    for line in text:
        line = line.rstrip()
        restaurant_data = line.split(":")
        restaurant = restaurant_data[0]
        rating = restaurant_data[1]
        restaurant_ratings[restaurant] = rating

    return restaurant_ratings


def get_rating(filename):
    """prompt user for input
    add input to current dictionary
    print the whole dictionary as nice print statements
    """

    restaurant_ratings = make_restaurant_dict(filename)

    user_restaurant = raw_input("Please enter a restaurant name: ")
    user_rating = raw_input("Please enter this restaurant's rating: ")

    restaurant_ratings[user_restaurant] = user_rating

    sorted_restaurants = sorted(restaurant_ratings.items())

    # Prints and rating in a readable format.
    for restaurant, rating in sorted_restaurants:
        print "{} is rated at {}.".format(restaurant, rating)

    return restaurant_ratings

get_rating(sys.argv[1])
