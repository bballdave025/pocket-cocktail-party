import numpy as np

from pocket_cocktail_party.geometry import (
    add_equal_room_mic,
    pentagon_bleed_matrix,
)


def test_pentagon_bleed_matrix_shape():
    matrix = pentagon_bleed_matrix()
    assert matrix.shape == (5, 5)


def test_pentagon_bleed_matrix_values():
    matrix = pentagon_bleed_matrix(adjacent_gain=0.2)
    phi = (1.0 + np.sqrt(5.0)) / 2.0
    assert matrix[0, 0] == 1.0
    assert np.isclose(matrix[0, 1], 0.2)
    assert np.isclose(matrix[0, 2], 0.2 / phi)


def test_add_equal_room_mic():
    matrix = pentagon_bleed_matrix()
    augmented = add_equal_room_mic(matrix, room_gain=0.3)
    assert augmented.shape == (6, 5)
    assert np.allclose(augmented[-1], 0.3)
