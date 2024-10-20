import unittest
from movie import Movie, PriceStrategy, price_code_for_movie
import datetime  # Import datetime module

class PricingTest(unittest.TestCase):

    def test_new_release(self):
        """Test that a movie released this year returns NEW_RELEASE"""
        current_year = datetime.datetime.now().year
        movie = Movie("Top Gun: Maverick", current_year, {"Action"}, PriceStrategy.REGULAR)
        self.assertEqual(price_code_for_movie(movie), PriceStrategy.NEW_RELEASE)

    def test_childrens_movie(self):
        """Test that a children's movie returns CHILDRENS"""
        movie = Movie("Frozen", 2013, {"Animation", "Children"}, PriceStrategy.REGULAR)
        self.assertEqual(price_code_for_movie(movie), PriceStrategy.CHILDRENS)

    def test_regular_movie(self):
        """Test that a regular movie returns REGULAR"""
        movie = Movie("The Martian", 2015, {"Drama", "Sci-Fi"}, PriceStrategy.REGULAR)
        self.assertEqual(price_code_for_movie(movie), PriceStrategy.REGULAR)
