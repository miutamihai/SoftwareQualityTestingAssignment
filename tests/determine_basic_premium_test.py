from functions.determine_basic_premium import determine_basic_premium


def determine_basic_premium_test():
    print('Premium test is running...')
    assert determine_basic_premium('Comprehensive') == 0.04
    assert determine_basic_premium('Third party') == 0.025
