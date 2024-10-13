from rental import Rental
from movie import Movie


class Customer:
    """A customer who rents movies.

    The customer object holds information about the
    movies rented for the current billing period,
    and can print a statement of his rentals.
    """

    def __init__(self, name: str):
        """Initialize a new customer."""
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        """Add a rental for this customer."""
        if rental not in self.rentals:
            self.rentals.append(rental)

    def get_name(self):
        """Get the customer's name."""
        return self.name

    def get_total_charge(self) -> float:
        """Calculate the total charge for all rentals."""
        return sum(rental.get_price() for rental in self.rentals)

    def get_total_renter_points(self) -> int:
        """Calculate the total frequent renter points for all rentals."""
        return sum(rental.rental_points() for rental in self.rentals)

    def statement(self):
        """Create a statement of rentals for the current period.

        Print all the rentals in the current period,
        along with total charges and frequent renter points.

        Returns:
            the statement as a String
        """
        total_amount = 0   # total rental charges
        frequent_renter_points = 0
        # the .format method substitutes actual values into the fmt string
        statement = f"Rental Report for {self.name}\n\n"
        header_fmt = "{:40s}  {:6s} {:6s}\n"
        statement += header_fmt.format("Movie Title", "  Days", " Price")
        rental_fmt = "{:40s}  {:6d} {:6.2f}\n"

        for rental in self.rentals:
            #  add a detail line to statement
            statement += rental_fmt.format(
                            rental.get_movie().get_title(),
                            rental.get_days_rented(),
                            rental.get_price())

        # Accumulate frequent renter points using self.get_total_renter_points()
        frequent_renter_points = self.get_total_renter_points()
        # footer: summary of charges
        statement += "\n"
        statement += "{:40s}  {:6s} {:6.2f}\n".format(
                       "Total Charges", "", self.get_total_charge())
        statement += "Frequent Renter Points earned: {}\n".format(frequent_renter_points)

        return statement
