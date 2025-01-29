# WordSaladSolver

**WordSaladSolver** is a Python program designed to solve the word game *Word Salad*. This game involves connecting letters on a 4x4 board to form words. The solver uses word encodings to identify possible words based on a provided theme and matches them as closely as possible to the board. 
**The web version of this game can be found here** https://wordsalad.online/

## How It Works

1. **Input the Board**: Enter your 4x4 board by modifying the `board` variable at the top of the program. Each letter represents a cell in the board.  
2. **Specify the Theme**: Input the puzzle's theme to guide the solver in finding relevant words.
3. **Specify Word Lengths**: This helps the program run more efficiently, only processing words that fit the desired word lengths.
4. **Run the Solver**: The program uses the board and theme to find and suggest words that fit as closely as possible.  

The program leverages word encodings to identify words on the board that align with the theme, helping you solve the puzzle efficiently.

## Features

- Supports custom 4x4 board configurations.  
- Allows the input of a theme for context-based word finding.  
- Uses efficient algorithms and word encodings to find words quickly.  
- Offers suggestions that match the theme as closely as possible.  

## Getting Started


### Installation

1. Clone the repository:  
   `git clone https://github.com/wjwarner24/WordSaladSolver.git`  
   `cd WordSaladSolver`  
2. Install required packages:  
   `pip install sentence-transformers` 

### Usage

1. Open the `solver.py` file in a text editor.  
2. Update the `board` variable at the top of the file with your board configuration, using a 4x4 array:  
   `board = [ ['t', 'h', 'i', 's'], ['i', 's', 'a', 'n'], ['e', 'x', 'a', 'm'], ['p', 'l', 'e', ' '] ]`  
3. Specify the theme for the puzzle in the `description` variable:  
   `description = "examples"`  
4. Run the program:  
   `python3 solver.py`  

## Example

### Input

`grid = [ ['c', 'a', 't', 's'], ['d', 'o', 'g', 's'], ['b', 'i', 'r', 'd'], ['f', 'i', 's', 'h'] ]`  
`theme = "animals"`  

### Output

`Possible words that fit the theme:`  
`- CATS`  
`- DOGS`  
`- BIRDS`  
`- FISH`  

## Contributing

Contributions are welcome! If you'd like to improve the solver, fix bugs, or add features, feel free to fork the repository and open a pull request.


## Acknowledgments

Special thanks to the creators of *Word Salad* for the inspiration, and to the open-source community for providing tools and resources.

---

Happy solving! 🎉

