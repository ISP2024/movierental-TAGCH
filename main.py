# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie, PriceStrategy
from rental import Rental
from customer import Customer


def make_movies():
    """Some sample movies."""
    movies = [
        Movie("Air", 2020, {"Drama", "Action"}, PriceStrategy.NEW_RELEASE),
        Movie("Oppenheimer", 2023, {"Biography", "Drama"}, PriceStrategy.REGULAR),
        Movie("Frozen", 2013, {"Animation", "Family"}, PriceStrategy.CHILDRENS),
        Movie("Bitconned", 2021, {"Action", "Thriller"}, PriceStrategy.NEW_RELEASE),
        Movie("Particle Fever", 2013, {"Documentary"}, PriceStrategy.REGULAR)
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days = (days + 2) % 5 + 1
    print(customer.statement())
