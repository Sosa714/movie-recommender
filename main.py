from src.data_processing import load_data, basic_statistics, preprocess_movies_data, preprocess_ratings_data,  preprocess_tags_data

def main():
    # Step 1: Exploring the Data
    movies = load_data("movies.csv")
    ratings = load_data("ratings.csv")
    tags = load_data("tags.csv")

    print("\nMovies Data:")
    basic_statistics(movies)

    print("\nRatings Data:")
    basic_statistics(ratings)

    print("\nTags Data:")
    basic_statistics(tags)

    # Step 2: Data Preprocessing
    '''
    movies = preprocess_movies_data(movies)
    ratings = preprocess_ratings_data(ratings)
    '''
    tags = preprocess_tags_data(tags)

    print("\nNew Tags Data:")
    basic_statistics(tags)

    # Merging data to be added here if necessary

if __name__ == "__main__":
    main()