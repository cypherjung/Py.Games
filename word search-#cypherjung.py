#word search

import random

# Function to generate a random word search grid
def generate_word_search(size):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    grid = [['_' for _ in range(size)] for _ in range(size)]
    for row in range(size):
        for col in range(size):
            grid[row][col] = random.choice(alphabet)
    return grid

# Function to display the word search grid
def display_grid(grid):
    for row in grid:
        print(' '.join(row))

# Function to find words in the word search grid
def find_words(grid, words):
    found_words = []
    size = len(grid)
    for word in words:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for row in range(size):
            for col in range(size):
                for direction in directions:
                    dx, dy = direction
                    found = True
                    for i in range(len(word)):
                        new_row = row + i * dx
                        new_col = col + i * dy
                        if new_row < 0 or new_row >= size or new_col < 0 or new_col >= size or grid[new_row][new_col] != word[i]:
                            found = False
                            break
                    if found:
                        found_words.append(word)
                        break
                if found:
                    break
            if found:
                break
    return found_words

# Main program
def main():
    size = int(input("Enter the size of the word search grid: "))
    word_list = input("Enter the words to search (separated by spaces): ").split()
    
    # Generate the word search grid
    grid = generate_word_search(size)
    
    # Find the words in the grid
    found_words = find_words(grid, word_list)
    
    # Display the grid and found words
    print("\nWord Search Grid:")
    display_grid(grid)
    print("\nFound Words:")
    if found_words:
        print(', '.join(found_words))
    else:
        print("No words found.")

# Run the program
if __name__ == "__main__":
    main()



