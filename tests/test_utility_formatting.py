import pytest
import torchspy


@pytest.mark.parametrize("num_bytes, expected_string",
                         ((1000, "1 KB"), (132.3, "132 B"), (10**7*1.3, "13 MB"), (10**10, "10 GB")))
def test_bytes_human_readable(num_bytes, expected_string):
    output = torchspy.utility.formatting.bytes_human_readable(num_bytes)
    assert output == expected_string


@pytest.mark.parametrize("spacings, expected_string",
                         (([4, 6], "I   am    hungry"), ([3, 4], "I  am  hungry")))
def test_spaced_string(spacings, expected_string):
    output = torchspy.utility.formatting.spaced_string("I", "am", "hungry", spacings=spacings)
    assert output == expected_string


def test_spaced_string_non_matching():
    with pytest.raises(ValueError):
        torchspy.utility.formatting.spaced_string("I", "am", "hungry", spacings=[1])
    with pytest.raises(ValueError):
        torchspy.utility.formatting.spaced_string("I", "am", "hungry", spacings=[1, 2, 3])
