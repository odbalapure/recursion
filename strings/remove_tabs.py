def remove_tabs(string: str) -> str:
    """
    Remove tabs from a string
    :string: String
    :return: String with no tabs or spaces
    """
    if not string:
        return ""
    
    if string[0] == "\t" or string[0] == " ":
        return remove_tabs(string[1:])
    else:
        return string[0] + remove_tabs(string[1:])

print(remove_tabs("Hello\tWorld"))