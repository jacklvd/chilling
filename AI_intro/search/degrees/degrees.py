import csv
import sys
from util import Node, QueueFrontier

# Maps names to a set of corresponding actor_ids
names = {}

# Maps actor_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of actor_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["actor_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["actor_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = actor_id_for_name(input("Name: "))
    if source is None:
        sys.exit("actor not found.")
    target = actor_id_for_name(input("Name: "))
    if target is None:
        sys.exit("actor not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            actor1 = people[path[i][1]]["name"]
            actor2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {actor1} and {actor2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, actor_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """
    # TODO: Initialise a BFS, with the starting actor ID:
    explored = set([])
    wiki = [source]
    dataset = {}
    
    while len(wiki) > 0:
        actor = wiki.pop(0)
        if actor == target:
            break
        explored.add(actor)
        for (movie, person) in neighbors_for_actor(actor):
            if not person in wiki and not person in explored:
                wiki.append(person)
                dataset[person] = (movie, actor)
    if not target in dataset:
        print(f'They do not have any common movies')
        return None
    
    path = []
    actor = target
    
    while actor != source:
        movie, person = dataset[actor]
        path.append((movie, actor))
        actor = person
        
    path.reverse()
    return path     


def actor_id_for_name(name):
    """
    Returns the IMDB id for a actor's name,
    resolving ambiguities as needed.
    """
    actor_ids = list(names.get(name.lower(), set()))
    if len(actor_ids) == 0:
        return None
    elif len(actor_ids) > 1:
        print(f"Which '{name}'?")
        for actor_id in actor_ids:
            actor = people[actor_id]
            name = actor["name"]
            birth = actor["birth"]
            print(f"ID: {actor_id}, Name: {name}, Birth: {birth}")
        try:
            actor_id = input("Intended actor ID: ")
            if actor_id in actor_ids:
                return actor_id
        except ValueError:
            pass
        return None
    else:
        return actor_ids[0]


def neighbors_for_actor(actor_id):
    """
    Returns (movie_id, actor_id) pairs for people
    who starred with a given actor.
    """
    movie_ids = people[actor_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for actor_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, actor_id))
    return neighbors


if __name__ == "__main__":
    main()
