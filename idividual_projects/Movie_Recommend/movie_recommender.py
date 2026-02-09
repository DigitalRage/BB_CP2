import csv

while True:
    try:
        # Try to open the CSV file
        with open("idividual_projects/Movie_Recommend/movie_recommender.py", mode="r") as csv_file:
            reader = csv.reader(csv_file)

            # Read the header row first
            headers = next(reader)

            # Store each movie as a dictionary
            movies = []
            for line in reader:
                # Create a dictionary using the header names
                movie = {
                    "title": line[0].strip(),
                    "director": line[1].strip().lower(),
                    "genres": [g.strip().lower() for g in line[2].split("/")],
                    "rating": line[3].strip(),
                    "length": int(line[4]) if line[4].isdigit() else None,
                    "actors": [a.strip().lower() for a in line[5].split(",")]
                }
                movies.append(movie)

    except:
        print("Can't find movies.csv — make sure it is in the same folder.")
    else:
        print("Movie list loaded successfully.\n")
        break


# Filter functions (simple, direct, readable)

def filter_by_genre(movie_list, genre):
    genre = genre.lower().strip()
    return [m for m in movie_list if any(genre in g for g in m["genres"])]

def filter_by_director(movie_list, director):
    director = director.lower().strip()
    return [m for m in movie_list if director in m["director"]]

def filter_by_actor(movie_list, actor):
    actor = actor.lower().strip()
    return [m for m in movie_list if any(actor in a for a in m["actors"])]

def filter_by_length(movie_list, min_len, max_len):
    results = []
    for m in movie_list:
        if m["length"] is None:
            continue
        if min_len is not None and m["length"] < min_len:
            continue
        if max_len is not None and m["length"] > max_len:
            continue
        results.append(m)
    return results


# Helper function to print movies

def print_movies(movie_list):
    if not movie_list:
        print("No movies found.\n")
        return

    for m in movie_list:
        print(f"Title: {m['title']}")
        print(f"Director: {m['director'].title()}")
        print(f"Genres: {', '.join(m['genres'])}")
        print(f"Actors: {', '.join(m['actors'])}")
        print(f"Length: {m['length']} min\n")


# Main program loop (simple while True like your example)

while True:
    print("MAIN MENU")
    print("1. Search / Get Recommendations")
    print("2. Print Full Movie List")
    print("3. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        # Ask which filters to use
        print("\nChoose filters (e.g., 1,3):")
        print("1. Genre")
        print("2. Director")
        print("3. Actor")
        print("4. Length (min/max)")

        selected = input("Your selection: ").strip()

        try:
            selected_filters = [int(x.strip()) for x in selected.split(",")]
        except:
            print("Invalid input.\n")
            continue

        # Start with all movies
        results = movies

        # Apply filters one at a time
        if 1 in selected_filters:
            g = input("Enter genre: ")
            results = filter_by_genre(results, g)

        if 2 in selected_filters:
            d = input("Enter director: ")
            results = filter_by_director(results, d)

        if 3 in selected_filters:
            a = input("Enter actor: ")
            results = filter_by_actor(results, a)

        if 4 in selected_filters:
            min_raw = input("Min length (blank for none): ").strip()
            max_raw = input("Max length (blank for none): ").strip()

            min_len = int(min_raw) if min_raw.isdigit() else None
            max_len = int(max_raw) if max_raw.isdigit() else None

            results = filter_by_length(results, min_len, max_len)

        # Show results
        print("\nResults:\n")
        print_movies(results)

    elif choice == "2":
        print("\nFull Movie List:\n")
        print_movies(movies)

    elif choice == "3":
        print("Goodbye.")
        break

    else:
        print("Invalid choice.\n")
