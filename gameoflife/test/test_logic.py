from gameoflife.logic import Game


def test_num_of_neighbors_none():
    # Given a board
    game = Game(3, 3)

    # When I calculate the neighbors of a lone cell
    game.cells[2][2] = 1
    neighbors = game.num_of_neighbors(2, 2)

    # I get no neighbors back
    assert neighbors == 0


def test_num_of_neighbors():
    # Given a board
    game = Game(5, 5)

    # When I calculate the neighbors of cells with neighbors
    game.cells = [
        [1, 0, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0],
    ]

    # I get the correct number of neighbors back
    assert game.num_of_neighbors(0, 0) == 0
    assert game.num_of_neighbors(0, 4) == 1
    assert game.num_of_neighbors(0, 3) == 2
    assert game.num_of_neighbors(2, 0) == 3
    assert game.num_of_neighbors(2, 3) == 4
    assert game.num_of_neighbors(4, 2) == 5
    assert game.num_of_neighbors(3, 3) == 6
    assert game.num_of_neighbors(3, 2) == 7
    assert game.num_of_neighbors(3, 1) == 8
