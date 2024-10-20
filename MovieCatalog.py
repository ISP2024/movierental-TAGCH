import csv
import logging
from typing import Optional
from movie import Movie, PriceStrategy

# Configure logging
logging.basicConfig(level=logging.ERROR)

class MovieCatalog:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
            cls._instance.movies = {}
            cls._instance.load_movies('movies.csv')  # Load movies from CSV file
        return cls._instance

    def load_movies(self, filename: str):
        """Load movies from a CSV file."""
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for line_number, row in enumerate(reader, start=1):
                if not row or row[0].startswith('#'):  # Skip blank and comment lines
                    continue
                
                try:
                    if len(row) < 4:
                        raise ValueError("Not enough fields")

                    movie_id, title, year_str, genres_str = row
                    year = int(year_str)
                    genres = [genre.strip() for genre in genres_str.split('|')]

                    # Create Movie object and store it in the dictionary
                    movie = Movie(title, year, set(genres), PriceStrategy.REGULAR)  # Default price strategy
                    self.movies[title.lower()] = movie  # Store by title (case insensitive)
                except ValueError as e:
                    logging.error(f"Line {line_number}: Unrecognized format \"{','.join(row)}\" - {e}")
                except Exception as e:
                    logging.error(f"Line {line_number}: Error processing \"{','.join(row)}\": {e}")

    def get_movie(self, title: str, year: Optional[int] = None) -> Optional[Movie]:
        """Get a movie by title and optional year."""
        title_lower = title.lower()
        if title_lower in self.movies:
            movie = self.movies[title_lower]
            if year is None or movie.year == year:
                return movie
        return None


# Example usage:
if __name__ == "__main__":
    catalog = MovieCatalog()
    movie = catalog.get_movie("Mulan")
    if not movie:
        print("Sorry, couldn't find that movie.")
    else:
        print(movie)
