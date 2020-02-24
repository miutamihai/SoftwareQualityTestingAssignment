from tests.determine_basic_premium_test import determine_basic_premium_test
from tests.handle_penalty_points_test import handle_penalty_points_test


def run_all_tests():
    determine_basic_premium_test()
    handle_penalty_points_test()


class Config(object):
    SECRET_KEY = 'S@FtW@rETeStinG'
