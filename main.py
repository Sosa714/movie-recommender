from src.data_processing import load_data

def main():
    # Step 1: Exploring the Data
    movies = load_data("movies.csv")
    ratings = load_data("ratings.csv")

if __name__ == "__main__":
    main()