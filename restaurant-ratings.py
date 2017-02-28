import sys


def print_ratings(filename):
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

    # Prints and rating in a readable format.
    for restaurant, rating in restaurant_ratings.items():
        print "{} is rated at {}.".format(restaurant, rating)


print_ratings(sys.argv[1])
