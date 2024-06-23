import re


def bin_filter(min_: str, max_: str) -> list:
    pattern = r'^\d+-\d+$'

    if min_.count("-") > 1 or max_.count("-") > 1:
        raise ValueError("Invalid format for min_ or max_")

    if not bool(re.match(pattern, min_)) or not bool(re.match(pattern, max_)):
        raise ValueError("Invalid format for min_ or max_")

    min_int: int = int(min_.split("-")[0])
    max_int: int = int(max_.split("-")[1])

    if max_int < min_int:
        raise ValueError("The minimum is larger than the maximum")

    if min_ == max_:
        raise ValueError("min_ and max_ are the same")

    return [i for i in range(min_int, max_int + 1)]
