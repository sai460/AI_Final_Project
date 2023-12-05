import random
import time
import matplotlib.pyplot as plt
import sys

def choose_difficulty():
    print("Select the difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    while True:
        try:
            choice = int(input("Enter the number corresponding to the desired difficulty level (1-3): "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Please enter a valid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_sudoku_puzzle_with_difficulty(n, difficulty_level):
    grid = [[0 for _ in range(n)] for _ in range(n)]

    fill_diagonal_subgrids(grid, n)
    solve_sudoku_optimized(grid, n)

    # Calculate the total number of cells to be removed
    total_cells = n * n
    if difficulty_level == 1:
        remove_percentage = 0.4  # Easy: 40% filled cells
    elif difficulty_level == 2:
        remove_percentage = 0.5  # Medium: 50% filled cells
    else:
        remove_percentage = 0.7  # Hard: 70% filled cells

    remove_count = int(total_cells * (1-remove_percentage))

    # Use random.sample to select cells to be removed
    cells_to_remove = random.sample(range(total_cells), remove_count)

    for cell in cells_to_remove:
        row = cell // n
        col = cell % n
        grid[row][col] = 0

    return grid

def solve_sudoku(grid, n, metrics=None):
    if metrics is None:
        metrics = {'recursive_calls': 0, 'backtracks': 0, 'max_depth': 0, 'subgrid_times': []}

    def inner_solve(row, col):
        metrics['recursive_calls'] += 1
        if row == n:
            return True  # Solved the entire grid

        next_row, next_col = (row, col + 1) if col + 1 < n else (row + 1, 0)

        if grid[row][col] != 0:
            # Move to the next cell if the current cell is pre-filled
            return inner_solve(next_row, next_col)

        for num in range(1, n + 1):
            if is_valid_entry(grid, row, col, num):
                grid[row][col] = num

                if inner_solve(next_row, next_col):
                    return True  # If the current configuration leads to a solution

                grid[row][col] = 0  # If the current configuration does not lead to a solution, backtrack
                metrics['backtracks'] += 1

        return False

    def get_max_depth(row, col, depth):
        metrics['max_depth'] = max(metrics['max_depth'], depth)
        return depth

    def solve_subgrid(row, col, subgrid_size):
        start_time = time.time()

        subgrid_solved = inner_solve(row, col)

        end_time = time.time()
        metrics['subgrid_times'].append(end_time - start_time)

        return subgrid_solved

    solve_subgrid(0, 0, n)

    return metrics

def solve_sudoku_optimized(grid, n, metrics=None):
    if metrics is None:
        metrics = {'recursive_calls': 0, 'backtracks': 0, 'max_depth': 0, 'subgrid_times': []}

    def solve_sudoku_optimized_recursive(row, col, subgrid_size, available_choices):
        metrics['recursive_calls'] += 1
        if row == n:
            return True  # Solved the entire grid

        next_row, next_col = (row, col + 1) if col + 1 < n else (row + 1, 0)

        if grid[row][col] != 0:
            # Move to the next cell if the current cell is pre-filled
            return solve_sudoku_optimized_recursive(next_row, next_col, subgrid_size, available_choices)

        for num in list(available_choices):
            if is_valid_entry(grid, row, col, num):
                grid[row][col] = num
                available_choices.remove(num)

                if solve_sudoku_optimized_recursive(next_row, next_col, subgrid_size, available_choices):
                    return True  # If the current configuration leads to a solution

                grid[row][col] = 0  # If the current configuration does not lead to a solution, backtrack
                metrics['backtracks'] += 1
                available_choices.add(num)

        return False

    def get_max_depth(row, col, depth):
        metrics['max_depth'] = max(metrics['max_depth'], depth)
        return depth

    def solve_subgrid(row, col, subgrid_size):
        start_time = time.time()

        solve_sudoku_optimized_recursive(row, col, subgrid_size, set(range(1, n + 1)))

        end_time = time.time()
        metrics['subgrid_times'].append(end_time - start_time)

    solve_subgrid(0, 0, n)

    return metrics

def get_available_choices(grid, row, col, n):
    # Use a set to store available choices
    choices = set(range(1, n + 1))

    # Remove choices in the same row and column
    choices -= set(grid[row])
    choices -= set(grid[i][col] for i in range(n))

    # Remove choices in the same subgrid
    subgrid_size = int(n ** 0.5)
    start_row, start_col = subgrid_size * (row // subgrid_size), subgrid_size * (col // subgrid_size)
    choices -= set(grid[i][j] for i in range(start_row, start_row + subgrid_size) for j in range(start_col, start_col + subgrid_size))
    return list(choices)
    
def is_valid_entry(grid, row, col, num):
    # Check if 'num' is not in the same row or column
    if num in grid[row] or num in [grid[i][col] for i in range(len(grid))]:
        return False

    # Check if 'num' is not in the same subgrid
    subgrid_size = int(len(grid) ** 0.5)
    start_row, start_col = subgrid_size * (row // subgrid_size), subgrid_size * (col // subgrid_size)
    for i in range(start_row, start_row + subgrid_size):
        for j in range(start_col, start_col + subgrid_size):
            if grid[i][j] == num:
                return False
    return True

def remove_numbers(grid, n):
    for row in grid:
        empty_col = random.randint(0, n - 1)
        row[empty_col] = 0

def find_empty_cell(grid, n):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                return i, j  # Return the first empty cell (row, column)
    return None

def fill_diagonal_subgrids(grid, n):
    subgrid_size = int(n ** 0.5)
    for i in range(0, n, subgrid_size):
        fill_subgrid(grid, i, i, subgrid_size)

def fill_subgrid(grid, start_row, start_col, subgrid_size):
    num_list = list(range(1, subgrid_size + 1))
    random.shuffle(num_list)
    index = 0
    for i in range(subgrid_size):
        for j in range(subgrid_size):
            if index < len(num_list):
                grid[start_row + i][start_col + j] = num_list[index]
                index += 1

def print_sudoku(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def visualize_metrics(metrics_backtracking, metrics_optimized, solver_names):
    labels = ['Recursive Calls', 'Backtracks', 'Max Depth']
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    
    # Backtracking - Metrics Distribution
    sizes_backtracking = [metrics_backtracking['recursive_calls'], metrics_backtracking['backtracks'], metrics_backtracking['max_depth']]
    axs[0, 0].pie(sizes_backtracking, labels=labels, autopct='%1.1f%%', startangle=90)
    axs[0, 0].axis('equal')
    axs[0, 0].set_title(f'{solver_names[0]} - Metrics Distribution')

    # Backtracking - Subgrid Solving Times
    axs[0, 1].bar(range(1, len(metrics_backtracking['subgrid_times']) + 1), metrics_backtracking['subgrid_times'], label=solver_names[0])
    axs[0, 1].set_xlabel('Subgrid')
    axs[0, 1].set_ylabel('Time (seconds)')
    axs[0, 1].set_title(f'{solver_names[0]} - Subgrid Solving Times')

    # Optimized Backtracking - Metrics Distribution
    sizes_optimized = [metrics_optimized['recursive_calls'], metrics_optimized['backtracks'], metrics_optimized['max_depth']]
    axs[1, 0].pie(sizes_optimized, labels=labels, autopct='%1.1f%%', startangle=90)
    axs[1, 0].axis('equal')
    axs[1, 0].set_title(f'{solver_names[1]} - Metrics Distribution')

    # Optimized Backtracking - Subgrid Solving Times
    axs[1, 1].bar(range(1, len(metrics_optimized['subgrid_times']) + 1), metrics_optimized['subgrid_times'], label=solver_names[1], alpha=0.5)
    axs[1, 1].set_xlabel('Subgrid')
    axs[1, 1].set_ylabel('Time (seconds)')
    axs[1, 1].set_title(f'{solver_names[1]} - Subgrid Solving Times')

    plt.show()
    plt.close()

def solve_and_measure_time(grid, n, solver_function, solver_name):
    start_time = time.time()

    metrics = solver_function(grid, n)

    end_time = time.time()
    print(f"\n{solver_name} - Solved Sudoku Puzzle:")
    print_sudoku(grid)
    print(f"\nTime taken to solve: {end_time - start_time:.4f} seconds")
    print(f"Number of Recursive Calls: {metrics['recursive_calls']}")
    print(f"Number of Backtracks: {metrics['backtracks']}")

   
    if 'subgrid_times' in metrics and metrics['subgrid_times']:
        avg_subgrid_time = sum(metrics['subgrid_times']) / len(metrics['subgrid_times'])
        print(f"Average Time per Subgrid: {avg_subgrid_time:.4f} seconds")
        print(f"Subgrid Solving Times: {metrics['subgrid_times']}")
    else:
        print("No subgrid solving times available.")
    return metrics

if __name__ == "__main__":
    solver_names = ['Backtracking', 'Optimized Backtracking']

    try:
        n = int(input("Enter the size of the Sudoku grid (e.g., 4 for 4x4, 9 for 9x9): "))
        if n <= 0 or (int(n**0.5))**2 != n:
            print("Please enter a positive square number.")
            sys.exit()

        difficulty_level = choose_difficulty()

        puzzle = generate_sudoku_puzzle_with_difficulty(n, difficulty_level)

        print("\nGenerated Sudoku Puzzle:")
        print_sudoku(puzzle)

        metrics_backtracking = solve_and_measure_time(puzzle, n, solve_sudoku, solver_names[0])
        metrics_optimized = solve_and_measure_time(puzzle, n, solve_sudoku_optimized, solver_names[1])

        # Visualize metrics
        visualize_metrics(metrics_backtracking, metrics_optimized, solver_names)

    except ValueError:
        print("Invalid input. Please enter a valid number.")
