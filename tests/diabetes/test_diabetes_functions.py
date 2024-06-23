import pytest

from diabetes_functions import bin_filter


@pytest.mark.parametrize("min_,max_,expected", [
    ("10-20", "20-30", list(range(10, 31))),  # Normaler Fall
    ("30-40", "40-50", list(range(30, 51))),  # Normaler Fall
    ("20-10", "20-10", ValueError),  # Fehlerfall: min_ ist größer als max_
    ("10-20", "10-20", ValueError),  # Fehlerfall: min_ und max_ sind gleich
    ("abc-20", "abc-20", ValueError),  # Fehlerfall: Ungültiges Format für min_
    ("10-abc", "10-abc", ValueError),  # Fehlerfall: Ungültiges Format für max_
    ("10-20-30", "10-20-30", ValueError),  # Fehlerfall: Mehr als ein Bindestrich in min_ oder max_
])
def test_bin_filter(min_, max_, expected):
    if isinstance(expected, list):
        assert bin_filter(min_, max_) == expected
    else:
        with pytest.raises(expected):
            bin_filter(min_, max_)
