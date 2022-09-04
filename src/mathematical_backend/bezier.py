import math


def linear_interpolate(start, end, current_time, total_time):
    percentage_time_elapsed = current_time / total_time  # not multiplying by 100 because will be used as a weighted sum
    interpolated_value = ((1 - percentage_time_elapsed) * start) + (percentage_time_elapsed * end)
    return interpolated_value


def quadratic_interpolate(start, end, middle, current_time, total_time):
    p1 = linear_interpolate(start, middle, current_time, total_time)
    p2 = linear_interpolate(middle, end, current_time, total_time)
    interpolated_value = linear_interpolate(p1, p2, current_time, total_time)
    return interpolated_value


def cubic_interpolate(start, end, middle1, middle2, current_time, total_time):
    p1 = quadratic_interpolate(start, middle2, middle1, current_time, total_time)
    p2 = quadratic_interpolate(middle1, end, middle2, current_time, total_time)
    interpolated_value = linear_interpolate(p1, p2, current_time, total_time)
    return interpolated_value


def ease(start, end, current_time, total_time):
    # Values taken from https://developer.mozilla.org/en-US/docs/Web/CSS/transition-timing-function#values
    middle1 = math.sqrt(
        (0.25 ** 2) + (0.1 ** 2)
    )
    middle2 = math.sqrt(
        (0.25 ** 2) + 1
    )

    interpolated_value = cubic_interpolate(start, end, middle1, middle2, current_time, total_time)
    return interpolated_value


def ease_in(start, end, current_time, total_time):
    # Values taken from https://developer.mozilla.org/en-US/docs/Web/CSS/transition-timing-function#values
    middle1 = math.sqrt(
        (0.25 ** 2) + (0.1 ** 2)
    )
    middle2 = math.sqrt(
        (0.25 ** 2) + 1
    )

    interpolated_value = cubic_interpolate(start, end, middle1, middle2, current_time, total_time)
    return interpolated_value


def ease_out(start, end, current_time, total_time):
    # Values taken from https://developer.mozilla.org/en-US/docs/Web/CSS/transition-timing-function#values
    middle1 = math.sqrt(
        (0.25 ** 2) + (0.1 ** 2)
    )
    middle2 = math.sqrt(
        (0.25 ** 2) + 1
    )

    interpolated_value = cubic_interpolate(start, end, middle1, middle2, current_time, total_time)
    return interpolated_value
