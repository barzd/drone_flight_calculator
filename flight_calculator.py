def calculate_flight_time(weight_grams):
    """Calculate the usable active flight time in minutes for a payload weight.

    Args:
        weight_grams (int or float): The payload weight in grams. Must be >= 0.

    Returns:
        float: The active flight time in minutes, calculated as 180 - 0.1 * weight_grams,
        with negative results clamped to 0.0.

 
    """
    if weight_grams < 0:
        raise ValueError("weight_grams must be non-negative.")

    return max(0.0, 180.0 - 0.1 * weight_grams)


def flight_time_table(max_weight_grams, step_grams):
    """Generate a table of payload weights and their corresponding flight times.

    Args:
        max_weight_grams (int or float): The maximum payload weight in grams to include.
        step_grams (int or float): The weight increment between rows. Must be > 0.

    Returns:
        list of tuple: A list of (weight, flight_time) pairs from 0 up to max_weight_grams,
        using step_grams increments.

    """
    if max_weight_grams < 0:
        raise ValueError("max_weight_grams must be non-negative.")
    if step_grams <= 0:
        raise ValueError("step_grams must be greater than 0.")

    table = []
    weight = 0

    while weight <= max_weight_grams:
        table.append((weight, calculate_flight_time(weight)))
        weight += step_grams

    return table