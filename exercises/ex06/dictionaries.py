"""Practice with dictionaries."""

__author__ = "730482618"

# Define your functions below


def invert(a: dict[str, str]) -> dict[str, str]:
    output: dict[str, str] = {}
    for key in a.keys():
        key_for_output = a[key] 
        output[key_for_output] = key
    return output


def favorite_color(a: dict[str, str]) -> str:
    colors: dict[str, int] = {}
    for students in a.keys():
        the_color = a[students]
        if the_color in colors.keys():
            colors[the_color] += 1
        else:
            colors[a[the_color]] = 1
    max_num = 0
    max_color = ""
    for color in colors:
        if colors[color] > max_num:
            max_num = colors[color]
            max_color = color
    return max_color