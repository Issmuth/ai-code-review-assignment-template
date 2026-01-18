def average_valid_measurements(values):
    if not values or not isinstance(values, (list, tuple)):
        return 0

    total = 0
    count = 0

    for v in values:
        try:
            if v is not None:
                total += float(v)
                count += 1
        except (ValueError, TypeError):
            continue

    return total / count if count != 0 else 0