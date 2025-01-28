

board = [
    [' ', ' ', 'a', 'd'],
    [' ', 'r', 'l', 'm'],
    [' ', 'o', 'e', 'e'],
    ['c', 's', 'o', 'n']
]


description = "colors"


lengths = {4, 5, 6, 7}


num_words_returned = 20













from sentence_transformers import SentenceTransformer, util

# Load words from the words.txt file
def load_words(file_path="words.txt"):
    with open(file_path, 'r') as file:
        # Read words and store them in a set
        return set(word.strip().lower() for word in file.readlines())
    

# Define the DFS-based function to explore the grid and find valid strings
def find_valid_strings(grid, words_set, allowed_lengths):
    rows, cols = 4, 4
    found_words = set()
    
    # Helper function to perform DFS on the grid
    def dfs(x, y, current_word, visited):
        if len(current_word) in allowed_lengths and current_word in words_set:
            found_words.add(current_word)

        if len(current_word) == 16:
            return
        
    
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] != ' ':
                visited.add((nx, ny))
                dfs(nx, ny, current_word + grid[nx][ny], visited)
                visited.remove((nx, ny))

    # Start DFS from each cell in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != ' ':
                dfs(i, j, grid[i][j], {(i, j)})
    
    return list(found_words)


# Gets the similarity between two strings
def bert_similarity(description, query):
    desc_embedding = model.encode(description)
    query_embedding = model.encode(query)
    similarity = util.cos_sim(desc_embedding, query_embedding).item()
    return similarity


# prints the top n words ranked by similarity
def get_top_n_words(valid_strings, prompt, n):
    similarity_scores = []
    
    for word in valid_strings:
            similarity_score = bert_similarity(prompt, word)
            similarity_scores.append((word, similarity_score))
    
    similarity_scores.sort(key=lambda x: x[1], reverse=True)
    
    print(f"\nTop {n} words ranked by similarity:")
    for word, score in similarity_scores[:n]:
        print(f"{word}: {score}")




# Load words dictionary (assuming a file `words.txt` is available)
words_set = load_words()
print(f"got {len(words_set)} words from the dictionary")

# Run the function on the example grid
valid_strings = find_valid_strings(board, words_set, lengths)
print(f"found {len(valid_strings)} valid strings")

# initialize the sentance tranformer model
# model = SentenceTransformer('all-MiniLM-L6-v2')
model = SentenceTransformer('multi-qa-mpnet-base-dot-v1')

# print the best matching words
get_top_n_words(valid_strings, description, num_words_returned)