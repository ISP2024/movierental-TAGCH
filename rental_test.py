import unittest
from movie import Movie, PriceStrategy
from rental import Rental, price_code_for_movie
import datetime

class RentalTest(unittest.TestCase):

    def setUp(self):
        current_year = datetime.datetime.now().year
        self.new_movie = Movie("Dune: Part Two", current_year, {"Action", "Adventure"}, PriceStrategy.REGULAR)
        self.regular_movie = Movie("Air", 2020, {"Drama", "Action"}, PriceStrategy.REGULAR)
        self.childrens_movie = Movie("Frozen", 2013, {"Animation", "Children"}, PriceStrategy.REGULAR)

    def test_rental_price_code_new_release(self):
        """Test that a rental of a new release movie has correct price code"""
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.price_code, PriceStrategy.NEW_RELEASE)

    def test_rental_price_code_childrens(self):
        """Test that a rental of a children's movie has correct price code"""
        rental = Rental(self.childrens_movie, 3)
        self.assertEqual(rental.price_code, PriceStrategy.CHILDRENS)

    def test_rental_price_code_regular(self):
        """Test that a rental of a regular movie has correct price code"""
        rental = Rental(self.regular_movie, 5)
        self.assertEqual(rental.price_code, PriceStrategy.REGULAR)
