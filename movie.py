from enum import Enum
from dataclasses import dataclass
from typing import Collection
import datetime

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


@dataclass(frozen=True)
class Movie:
    """A movie available for rent."""
    title: str
    year: int
    genre: Collection[str]
    price_strategy: PriceStrategy  # Add this attribute

    def is_genre(self, genre_name: str) -> bool:
        """Check if the movie belongs to the specified genre."""
        return genre_name.lower() in (g.lower() for g in self.genre)

    def get_title(self) -> str:
        """Return the title of the movie."""
        return self.title

    def __str__(self) -> str:
        """Return a string representation of the movie."""
        return f"{self.title} ({self.year})"


def price_code_for_movie(movie: Movie) -> PriceStrategy:
    """Determine the price code for a given movie."""
    current_year = datetime.datetime.now().year

    if movie.year == current_year:
        return PriceStrategy.NEW_RELEASE

    if any(genre.lower() in ["children", "childrens"] for genre in movie.genre):
        return PriceStrategy.CHILDRENS

    return PriceStrategy.REGULAR
