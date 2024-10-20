import re
import unittest 
from customer import Customer
from rental import Rental
from movie import Movie, PriceStrategy, price_code_for_movie
import datetime


class CustomerTest(unittest.TestCase): 
    """ Tests of the Customer class"""
    
    def setUp(self):
        """Test fixture contains:
        c = a customer
        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
        
        # Create movies with correct years
        current_year = datetime.datetime.now().year
        self.new_movie = Movie("Mulan", current_year, {"Animation", "Action"}, PriceStrategy.REGULAR)
        self.regular_movie = Movie("CitizenFour", 2014, {"Documentary"}, PriceStrategy.REGULAR)
        self.childrens_movie = Movie("Frozen", 2013, {"Animation", "Children"}, PriceStrategy.REGULAR)

    def test_get_total_charge(self):
        """Test the total charge calculation for multiple rentals."""
        # Add rentals and check total charge
        self.c.add_rental(Rental(self.new_movie, 4))  # Expecting NEW_RELEASE pricing
        self.c.add_rental(Rental(self.regular_movie, 3))  # Expecting REGULAR pricing
        self.c.add_rental(Rental(self.childrens_movie, 5))  # Expecting CHILDRENS pricing

        # Calculate expected charges based on pricing rules
        expected_charge = (price_code_for_movie(self.new_movie).get_price(4) + 
                           price_code_for_movie(self.regular_movie).get_price(3) + 
                           price_code_for_movie(self.childrens_movie).get_price(5))
        
        total_charge = self.c.get_total_charge()
        
        self.assertEqual(total_charge, expected_charge)

    def test_get_total_renter_points(self):
        """Test the total renter points calculation for multiple rentals."""
        # Add rentals and check frequent renter points
        self.c.add_rental(Rental(self.new_movie, 4))  # New release earns points based on days rented
        self.c.add_rental(Rental(self.regular_movie, 3))  # Regular movie earns 1 point
        self.c.add_rental(Rental(self.childrens_movie, 5))  # Children's movie earns 1 point

        # Total points should be calculated based on rules defined in price_code_for_movie
        total_points = self.c.get_total_renter_points()
        
        expected_points = (price_code_for_movie(self.new_movie).get_rental_points(4) + 
                           price_code_for_movie(self.regular_movie).get_rental_points(3) + 
                           price_code_for_movie(self.childrens_movie).get_rental_points(5))
        
        self.assertEqual(total_points, expected_points)
