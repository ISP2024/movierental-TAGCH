import unittest
from customer import Customer
from rental import Rental
from movie import Movie, PriceStrategy

class RentalTest(unittest.TestCase):

    def setUp(self):
    	self.new_movie = Movie("Dune: Part Two", 2023, {"Action", "Adventure"}, PriceStrategy.NEW_RELEASE)
    	self.regular_movie = Movie("Air", 2020, {"Drama", "Action"}, PriceStrategy.REGULAR)
    	self.childrens_movie = Movie("Frozen", 2013, {"Animation", "Family"}, PriceStrategy.CHILDRENS)

    def test_movie_attributes(self):
    	"""Trivial test to catch refactoring errors or change in API of Movie"""
    	m = Movie("Air", 2020, {"Drama"}, PriceStrategy.REGULAR)
    	self.assertEqual("Air", m.title)   # Directly access title attribute
    	self.assertEqual(2020, m.year)     # Check year attribute
    	self.assertIn("Drama", m.genre)    # Check genre attribute

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
