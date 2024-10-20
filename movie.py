from enum import Enum

class PriceStrategy(Enum):
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDRENS = 2

    def get_price(self, days_rented: int) -> float:
        """Calculate rental price based on the price strategy."""
        if self == PriceStrategy.REGULAR:
            amount = 2.0
            if days_rented > 2:
                amount += (days_rented - 2) * 1.5
            return amount
        elif self == PriceStrategy.NEW_RELEASE:
            return days_rented * 3
        elif self == PriceStrategy.CHILDRENS:
            amount = 1.5
            if days_rented > 3:
                amount += (days_rented - 3) * 1.5
            return amount
        else:
            raise ValueError("Unknown price strategy")

    def get_rental_points(self, days_rented: int) -> int:
        """Calculate rental points based on the price strategy."""
        if self == PriceStrategy.NEW_RELEASE:
            return days_rented
        return 1


class Movie:
    """
    A movie available for rent.
    """

    def __init__(self, title: str, price_strategy: PriceStrategy):
        """Initialize a new movie."""
        self.title = title
        self.price_strategy = price_strategy

    def get_title(self) -> str:
        """Get the movie title."""
        return self.title

    def __str__(self) -> str:
        return self.title
