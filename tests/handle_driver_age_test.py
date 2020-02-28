from functions.handle_driver_age import handle_driver_age


def handle_driver_age_test():
    driver_age_handler = handle_driver_age(17)
    assert driver_age_handler is False
    driver_age_handler = handle_driver_age(18)
    assert driver_age_handler == 0.10
    driver_age_handler = handle_driver_age(25)
    assert driver_age_handler is None

