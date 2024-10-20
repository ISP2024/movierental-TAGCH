from movie import Movie, price_code_for_movie

class Rental:
    """
    A rental of a movie by customer.
    """

    def __init__(self, movie: Movie, days_rented: int):
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = price_code_for_movie(movie)  # Determine price code from movie

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def get_price(self) -> float:
        """Calculate price using PriceStrategy from Rental's price code."""
        return self.price_code.get_price(self.days_rented)

    def rental_points(self) -> int:
        """Calculate rental points using PriceStrategy from Movie."""
        return self.price_code.get_rental_points(self.days_rented)
