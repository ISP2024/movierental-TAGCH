import re
import unittest
from customer import Customer
from rental import Rental
from movie import Movie, PriceStrategy

class CustomerTest(unittest.TestCase): 
    """ Tests of the Customer class"""
    
    def setUp(self):
    	"""Test fixture contains:
    	
    	c = a customer
    	movies = list of some movies
    	"""
    	self.c = Customer("Movie Mogul")
    	self.new_movie = Movie("Mulan", PriceStrategy.NEW_RELEASE)
    	self.regular_movie = Movie("CitizenFour", PriceStrategy.REGULAR)
    	self.childrens_movie = Movie("Frozen", PriceStrategy.CHILDRENS)

    @unittest.skip("No convenient way to test")
    def test_billing(self):
    	# no convenient way to test billing since its buried in the statement() method.
    	pass

    def test_statement(self):
    	stmt = self.c.statement()
    	# get total charges from statement using a regex
    	pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
    	matches = re.match(pattern, stmt, flags=re.DOTALL)
    	self.assertIsNotNone(matches)
    	self.assertEqual("0.00", matches[1])
    	# add a rental
    	self.c.add_rental(Rental(self.new_movie, 4)) # days
    	stmt = self.c.statement()
    	matches = re.match(pattern, stmt.replace('\n',''), flags=re.DOTALL)
    	self.assertIsNotNone(matches)
    	self.assertEqual("12.00", matches[1])

    def test_get_total_charge(self):
        """Test the total charge calculation for multiple rentals."""
        # No rentals, total charge should be 0
        self.assertEqual(self.c.get_total_charge(), 0.0)

        # Add rentals and check total charge
        self.c.add_rental(Rental(self.new_movie, 4))  # 12.00
        self.c.add_rental(Rental(self.regular_movie, 3))  # 3.50
        self.c.add_rental(Rental(self.childrens_movie, 5))  # 4.50

        # Total charge should be the sum of all rentals
        total_charge = self.c.get_total_charge()
        self.assertEqual(total_charge, 12.00 + 3.50 + 4.50)  # 20.00

    def test_get_total_renter_points(self):
        """Test the total renter points calculation for multiple rentals."""
        # No rentals, total points should be 0
        self.assertEqual(self.c.get_total_renter_points(), 0)

        # Add rentals and check frequent renter points
        self.c.add_rental(Rental(self.new_movie, 4))  # New release earns 4 points
        self.c.add_rental(Rental(self.regular_movie, 3))  # Regular movie earns 1 point
        self.c.add_rental(Rental(self.childrens_movie, 5))  # Children's movie earns 1 point

        # Total points should be the sum of all rentals
        total_points = self.c.get_total_renter_points()
        self.assertEqual(total_points, 4 + 1 + 1)  # 6 points
