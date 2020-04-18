from gameoflife.logic import Game


def test_num_of_neighbors():
    """ Test ability to calculate number of neighbors """
    # Given a board
    game = Game(5, 5)
    game.cells = [
        [1, 0, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0],
    ]

    # When I calculate the neighbors of cells with neighbors
    # Then I get the correct number of neighbors back
    assert game.num_of_neighbors(0, 0) == 0
    assert game.num_of_neighbors(0, 4) == 1
    assert game.num_of_neighbors(0, 3) == 2
    assert game.num_of_neighbors(2, 0) == 3
    assert game.num_of_neighbors(2, 3) == 4
    assert game.num_of_neighbors(4, 2) == 5
    assert game.num_of_neighbors(3, 3) == 6
    assert game.num_of_neighbors(3, 2) == 7
    assert game.num_of_neighbors(3, 1) == 8


def test_calculate_next_board():
    """ Test calculation of next board state """
    # Given a game board (Glider config)
    game = Game(5, 5)
    game.cells = [
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    # When I calculate the next board state
    # Then the rules of life are followed
    next_board = game.calculate_next_board()
    board_1 = [
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    assert next_board == board_1
