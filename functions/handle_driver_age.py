def handle_driver_age(driver_age):
    if driver_age < 18:
        return False
    elif driver_age < 25:
        return 0.10
    else:
        return None
