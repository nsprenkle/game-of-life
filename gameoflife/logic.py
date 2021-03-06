class Game:
    """ Containing class for cells in the Game of Life simulation """

    def __init__(self, y_max, x_max):
        """ Create a board with given y/x dimensions """
        self.y_max = y_max
        self.x_max = x_max
        self.cells = [[0 for x in range(x_max)] for y in range(y_max)]
        self.iteration = 0

    def num_of_neighbors(self, y, x):
        """ Calculate the number of neighbors of a cell """
        neighbors = 0

        y_range = [y - 1, y, y + 1]
        x_range = [x - 1, x, x + 1]

        for y_neighbor in y_range:

            # y bounds check
            if y_neighbor < 0:
                continue
            elif y_neighbor >= self.y_max:
                continue

            for x_neighbor in x_range:

                # x bounds check
                if x_neighbor < 0:
                    continue
                if x_neighbor >= self.x_max:
                    continue

                if self.cells[y_neighbor][x_neighbor] == 1:
                    neighbors += 1

        # remove self count of neighbor_x and neighbor_y = x, y
        if self.cells[y][x] == 1:
            neighbors -= 1

        return neighbors

    def update_board(self):
        """ Update the board to the next state """
        self.cells = self.calculate_next_board()
        self.iteration += 1

    def calculate_next_board(self):
        """
        Calculate the next board state based on the rules:

        For a space that is 'populated':
            Each cell with one or no neighbors dies, as if by solitude. 
            Each cell with four or more neighbors dies, as if by overpopulation. 
            Each cell with two or three neighbors survives. 
        For a space that is 'empty' or 'unpopulated'
            Each cell with three neighbors becomes populated. 
        """
        # Calculate neighbors for each cell
        neighbor_counts = [
            [self.num_of_neighbors(y, x) for x in range(self.x_max)]
            for y in range(self.y_max)
        ]

        # Generate next board
        next_board = [[0 for x in range(self.x_max)] for y in range(self.y_max)]

        for y in range(self.y_max):
            for x in range(self.x_max):
                neighbor_count = neighbor_counts[y][x]

                # Populated cell
                if self.cells[y][x] == 1 and neighbor_count in (2, 3):
                    next_board[y][x] = 1
                # Unpopulated cell
                elif self.cells[y][x] == 0 and neighbor_count == 3:
                    next_board[y][x] = 1
                else:
                    next_board[y][x] = 0

        return next_board

    def toggle_cell(self, y, x):
        """ Toggle the value of a cell at a given (y,x) coodinate. Return new value """
        if self.cells[y][x] == 1:
            self.cells[y][x] = 0
            return 0
        else:
            self.cells[y][x] = 1
            return 1
