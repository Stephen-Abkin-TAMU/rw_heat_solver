def Nuke_a_glob(frnt_glob, curr_glob, back_glob):
    # remove curr_glob from linked list
    prev_g = curr_glob.prev
    next_g = curr_glob.next

    if prev_g is not None and next_g is not None:
        prev_g.next = next_g
        next_g.prev = prev_g
        temp = next_g
    elif prev_g is None and next_g is not None:  # removing front
        frnt_glob = next_g
        frnt_glob.prev = None
        temp = frnt_glob
    else:  # removing back
        back_glob = prev_g
        back_glob.next = None
        temp = back_glob

    return frnt_glob, temp, back_glob
