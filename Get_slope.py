def Get_slope(curr_list, key):
    # key == 1 : first derivative
    # key == 2 : second derivative
    Sx = Sxx = Sy = Sxy = 0.0
    n = 0
    nodes = []
    if curr_list.prev is not None:
        nodes.append(curr_list.prev)
    nodes.append(curr_list)
    if curr_list.next is not None:
        nodes.append(curr_list.next)

    for node in nodes:
        x = node.location
        if key == 1:
            y = node.U
        else:
            y = node.Ux
        Sx += x
        Sxx += x * x
        Sy += y
        Sxy += x * y
        n += 1

    return (n * Sxy - Sx * Sy) / (n * Sxx - Sx * Sx)
