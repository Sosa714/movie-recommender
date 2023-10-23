from src.data_processing import load_data, basic_statistics

def main():
    # Step 1: Exploring the Data
    movies = load_data("movies.csv")
    ratings = load_data("ratings.csv")
    tags = load_data("tags.csv")
    genome_scores = load_data("genome-scores.csv")
    genome_tags = load_data("genome-tags.csv")

    print("\nMovies Data:")
    basic_statistics(movies)

    print("\nRatings Data:")
    basic_statistics(ratings)

    print("\nTags Data:")
    basic_statistics(tags)

    print("\nGenome Scores Data:")
    basic_statistics(genome_scores)

    print("\nGenome Tags Data:")
    basic_statistics(genome_tags)
    
if __name__ == "__main__":
    main()