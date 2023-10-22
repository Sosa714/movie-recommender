from src.data_processing import load_data, basic_statistics

def main():
    # Step 1: Exploring the Data
    movies = load_data("movies.csv")
    ratings = load_data("ratings.csv")

    print("\nMovies Data:")
    basic_statistics(movies)

    print("\nRatings Data:")
    basic_statistics(ratings)

if __name__ == "__main__":
    main()