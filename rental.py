from movie import Movie
import logging


class Rental:
    """
    A rental of a movie by customer.
    """

    def __init__(self, movie: Movie, days_rented: int):
        self.movie = movie
        self.days_rented = days_rented

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def get_price(self) -> float:
        """Calculate price using PriceStrategy from Movie."""
        return self.movie.price_strategy.get_price(self.days_rented)

    def rental_points(self) -> int:
        """Calculate rental points using PriceStrategy from Movie."""
        return self.movie.price_strategy.get_rental_points(self.days_rented)
