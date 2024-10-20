import unittest
from customer import Customer
from rental import Rental
from movie import Movie, PriceStrategy

class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", PriceStrategy.NEW_RELEASE)
        self.regular_movie = Movie("Air", PriceStrategy.REGULAR)
        self.childrens_movie = Movie("Frozen", PriceStrategy.CHILDRENS)

    def test_movie_attributes(self):
        """Trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air", PriceStrategy.REGULAR)
        self.assertEqual("Air", m.get_title())
        self.assertEqual(PriceStrategy.REGULAR, m.price_strategy)

    def test_rental_price(self):
        """Test the rental price calculation for various movie categories."""
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)

        rental = Rental(self.regular_movie, 2)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, 5)
        self.assertEqual(rental.get_price(), 6.5)

        rental = Rental(self.childrens_movie, 3)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.childrens_movie, 5)
        self.assertEqual(rental.get_price(), 4.5)

    def test_rental_points(self):
        """Test the calculation of frequent renter points for different categories."""
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.rental_points(), 1)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.rental_points(), 5)

        rental = Rental(self.regular_movie, 2)
        self.assertEqual(rental.rental_points(), 1)

        rental = Rental(self.childrens_movie, 5)
        self.assertEqual(rental.rental_points(), 1)
