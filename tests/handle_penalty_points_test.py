from functions.handle_penalty_points import handle_penalty_points


def handle_penalty_points_test():
    print('Penalty points test is running...')
    assert handle_penalty_points(0, 0) == (0, True)
    assert handle_penalty_points(0, 1) == (100, True)
    assert handle_penalty_points(0, 4) == (100, True)
    assert handle_penalty_points(0, 5) == (200, True)
    assert handle_penalty_points(0, 7) == (200, True)
    assert handle_penalty_points(0, 8) == (300, True)
    assert handle_penalty_points(0, 10) == (300, True)
    assert handle_penalty_points(0, 11) == (400, True)
    assert handle_penalty_points(0, 12) == (400, True)
    assert handle_penalty_points(0, 13) == (0, False)
