def value(colors):
    colors_map = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    total = 0
    for index, color in enumerate(colors):
        if index > 1:
            break
        total = total * 10 + colors_map.index(color)
    return total
