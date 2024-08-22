def remove_adjacent(string: str) -> str:
    """
    Remove adjacent duplicates
    :string: String
    :return: String with no adjacent duplicates
    """
    if not string:
        return ""
    elif len(string) == 1:
        return string
    elif string[0] == string[1]:
        return remove_adjacent(string[1:])
    return string[0] + remove_adjacent(string[1:])

print(remove_adjacent('Hii thereee!')) # Hi there!