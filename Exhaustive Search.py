import itertools
import math
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
def tsp(cities):
    start_city = cities[0]
    remaining_cities = cities[1:]
    all_permutations = itertools.permutations(remaining_cities)
    min_distance = float('inf')
    shortest_path = None
    for perm in all_permutations:
        current_route = [start_city] + list(perm) + [start_city]
        current_distance = 0
        for i in range(len(current_route) - 1):
            current_distance += distance(current_route[i], current_route[i+1])
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_path = current_route
    return min_distance, shortest_path
def test_tsp():
    cities1 = [(1, 2), (4, 5), (7, 1), (3, 6)]
    min_distance1, shortest_path1 = tsp(cities1)
    print("Test Case 1:")
    print(f"Shortest Distance: {min_distance1}")
    print(f"Shortest Path: {shortest_path1}\n")
    cities2 = [(2, 4), (8, 1), (1, 7), (6, 3), (5, 9)]
    min_distance2, shortest_path2 = tsp(cities2)
    print("Test Case 2:")
    print(f"Shortest Distance: {min_distance2}")
    print(f"Shortest Path: {shortest_path2}\n")
if __name__ == "__main__":
    test_tsp()
