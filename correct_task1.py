def calculate_average_order_value(orders):
    total = 0
    count = 0 # not the length of the list

    for order in orders:
        if order and order.get("status") != "cancelled":
            amount = order.get("amount", 0)
            if isinstance(amount, (int, float)):
                count += 1 #count non-cancelled/valid orders only
                total += amount

    return total / count if count != 0 else 0