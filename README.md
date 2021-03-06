# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Naked Twins
Q: How do we use constraint propagation to solve the naked twins problem?  
A: Naked twins is another technique that can be added to the sequence of techniques that are repeatedly applied to the problem (namely eliminate and reduce only). This may help us do less iterations by pruning the search space. This strategy allows us to remove the two values that appear in two peer boxes (could be vertical, horizontal, diagonal or any other type based on the rules of the game) from all the boxes that both of these boxes are peers with. This will allows us to cut out a whole bunch of possible values, reduce the search space, which will result in a faster solution to the game.

# Diagonal Sudoku
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: Constraint propagation is the technique of repeatedly applying a set of techniques to the problem. With diagonal sudoku there's an extra condition which is only applicable with the "only choice" technique. Expanding the list of units that this technique has to cover to include the diagonal units will address this constraint. The diagonal constraint increases the search space that has to be covered since there are more constraints (more peers per box). Computationally this constraint adds twice the number of rows peers to each box which has to be searched in the worst case scenario. This amounts to an extra `2 * rows * (rows * rows)` number of conditions (`2 * rows` extra constraints per box and we have `(rows * rows)` number of boxes) which is cubic in number of `rows` and can become intractable very quickly with increasing number of `rows`.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.