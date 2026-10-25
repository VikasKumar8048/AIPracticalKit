"""Experiment 6: Local Beam Search for the Traveling Salesman Problem."""

import itertools
import math
import random


def tour_cost(tour, distance):
    """Total cost of a tour, including the return to city 0."""
    total = 0
    n = len(tour)
    for i in range(n - 1):
        total += distance[tour[i]][tour[i + 1]]
    total += distance[tour[-1]][tour[0]]
    return total


def local_beam_tsp(distance, beam_width=3, max_iterations=20, seed=42):
    """Return the best tour found by Local Beam Search.

    City 0 is fixed at the beginning of each tour. `distance` is a square matrix.
    """
    n = len(distance)
    if n < 3 or any(len(row) != n for row in distance):
        raise ValueError("Distance matrix must be square and contain at least 3 cities.")
    if beam_width < 1 or max_iterations < 1:
        raise ValueError("Beam width and iterations must both be at least 1.")
    if any(distance[i][j] < 0 for i in range(n) for j in range(n)):
        raise ValueError("Distances cannot be negative.")

    beam_width = min(beam_width, math.factorial(n - 1))
    rng = random.Random(seed)
    city_list = list(range(1, n))
    beam = []
    seen = set()

    # Create distinct initial tours in a repeatable random order.
    attempts = 0
    while len(beam) < beam_width and attempts < beam_width * 50:
        rng.shuffle(city_list)
        tour = tuple([0] + city_list[:])
        if tour not in seen:
            seen.add(tour)
            beam.append(tour)
        attempts += 1

    # Fill any remaining slots systematically (small practical inputs).
    if len(beam) < beam_width:
        for order in itertools.permutations(range(1, n)):
            tour = tuple([0] + list(order))
            if tour not in seen:
                seen.add(tour)
                beam.append(tour)
            if len(beam) == beam_width:
                break

    best_tour = min(beam, key=lambda tour: tour_cost(tour, distance))
    best_cost = tour_cost(best_tour, distance)
    history = [best_cost]

    for _ in range(max_iterations):
        candidates = {}
        for tour in beam:
            for i in range(1, n - 1):
                for j in range(i + 1, n):
                    neighbour = list(tour)
                    neighbour[i], neighbour[j] = neighbour[j], neighbour[i]
                    neighbour = tuple(neighbour)
                    candidates[neighbour] = tour_cost(neighbour, distance)

        if not candidates:
            break

        ordered = sorted(candidates.items(), key=lambda item: (item[1], item[0]))
        next_beam = [tour for tour, cost_value in ordered[:beam_width]]
        beam = next_beam

        if ordered[0][1] < best_cost:
            best_tour = ordered[0][0]
            best_cost = ordered[0][1]
        history.append(best_cost)

    return {"tour": list(best_tour), "cost": best_cost,
            "iterations": len(history) - 1, "best_cost_history": history}


def run_cli():
    print("\nEXPERIMENT 6: LOCAL BEAM SEARCH FOR TSP")
    try:
        n = int(input("Enter number of cities (3-10 recommended): "))
        if n < 3 or n > 10:
            raise ValueError("Use between 3 and 10 cities for this practical.")
        distance = []
        print("Enter the distance matrix, one row per line:")
        for _ in range(n):
            row = [float(x) for x in input().split()]
            if len(row) != n:
                raise ValueError("Each distance row must contain exactly n values.")
            distance.append(row)
        beam_width = int(input("Enter beam width K: "))
        iterations = int(input("Enter maximum iterations: "))
        result = local_beam_tsp(distance, beam_width, iterations)
    except ValueError as error:
        print("Input error:", error)
        return

    tour = result["tour"]
    print("\nBest tour found:")
    print(" -> ".join(str(city) for city in tour + [tour[0]]))
    print("Best tour cost:", round(result["cost"], 3))
    print("Iterations completed:", result["iterations"])
    print("Note: Local Beam Search is heuristic and does not guarantee the global optimum.")


if __name__ == "__main__":
    run_cli()
