import itertools
def total_cost(assignment, cost_matrix):
    cost = 0
    for worker, task in enumerate(assignment):
        cost += cost_matrix[worker][task]
    return cost
def assignment_problem(cost_matrix):
    num_workers = len(cost_matrix)
    tasks = range(num_workers) 
    all_permutations = itertools.permutations(tasks)
    min_cost = float('inf') 
    best_assignment = None
    for perm in all_permutations:
        current_cost = total_cost(perm, cost_matrix)
        if current_cost < min_cost:
            min_cost = current_cost
            best_assignment = perm
    return min_cost, best_assignment
def print_results(cost_matrix, min_cost, best_assignment):
    formatted_assignment = [(f"worker {i+1}", f"task {task+1}") for i, task in enumerate(best_assignment)]
    print(f"Optimal Assignment: {formatted_assignment}")
    print(f"Total Cost: {min_cost}\n")
def test_assignment_problem():
    cost_matrix1 = [
        [3, 10, 7],
        [8, 5, 12],
        [4, 6, 9]
    ]
    min_cost1, best_assignment1 = assignment_problem(cost_matrix1)
    print("Test Case 1:")
    print_results(cost_matrix1, min_cost1, best_assignment1)
    cost_matrix2 = [
        [15, 9, 4],
        [8, 7, 18],
        [6, 12, 11]
    ]
    min_cost2, best_assignment2 = assignment_problem(cost_matrix2)
    print("Test Case 2:")
    print_results(cost_matrix2, min_cost2, best_assignment2)
if __name__ == "__main__":
    test_assignment_problem()
