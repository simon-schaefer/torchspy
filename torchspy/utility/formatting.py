import logging
from typing import List


def bytes_human_readable(num_bytes: int) -> str:
    """Convert bytes to a human-readable string such as 5 MB. Thereby, always round down to
    the next human-readable integer, i.e. 5400 bytes -> 5 MB.

    Args:
        num_bytes: number of bytes.
    Returns:
        string representation of bytes in (B, KB, MB, GB).
    """
    if num_bytes < 0:  # negative case
        return "-" + bytes_human_readable(-num_bytes)

    bytes_dict = {"GB": 10**9, "MB": 10**6, "KB": 10**3}
    for key, size in bytes_dict.items():
        if num_bytes >= size:
            num_bytes = int(num_bytes / size)
            return f"{num_bytes} {key}"
    return f"{int(num_bytes)} B"


def spaced_string(*args, spacings: List[int]) -> str:
    """Format string to always have the same number of characters between its elements, fill the remaining
    characters with spaces.

    >>> spaced_string("I", "am", "hungry", spacings=[3, 6])
    I  am    hungry

    Args:
        *args: Elements of string to combine to one string (len = k).
        spacings: Number of characters of each string part, including number of characters of element (len = k-1).
    """
    if len(args) == 0:
        return ""
    if len(args) != len(spacings) + 1:
        raise ValueError(f"Got non-matching strings spacings, got {len(args)} strings and {len(spacings)} spacing")
    if any(len(x) > spacing_i for x, spacing_i in zip(args[:-1], spacings)):
        logging.debug("At least one string is larger than its assigned spacing")
    output = ""
    for x, spacing in zip(args[:-1], spacings):
        output += x + " " * max(spacing - len(x), 0)
    return output + args[-1]
