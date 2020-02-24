def handle_penalty_points(premium, penalty_points):
    quote_possible = True
    if 1 <= penalty_points <= 4:
        premium += 100
    elif 5 <= penalty_points <= 7:
        premium += 200
    elif 8 <= penalty_points <= 10:
        premium += 300
    elif 11 <= penalty_points <= 12:
        premium += 400
    elif 12 < penalty_points:
        quote_possible = False
    return premium, quote_possible

