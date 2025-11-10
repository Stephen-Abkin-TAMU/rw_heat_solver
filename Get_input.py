from rw_header import Glob

def Get_input(input_file_name):
    """
    Reads the init file and returns (front_glob, back_glob, params_dict)
    """
    from rw_header import (
        left_end_exists, rite_end_exists, left_symmetric, rite_symmetric,
        left_end, rite_end
    )
    # we will *not* overwrite the module globals here to keep it simple;
    # instead we return them.
    with open(input_file_name, "r") as f:
        # first two lines: boundaries
        le_exists, le, le_sym = [x.strip() for x in f.readline().split(",")]
        re_exists, re, re_sym = [x.strip() for x in f.readline().split(",")]

        alpha = float(f.readline().strip())
        time_step = float(f.readline().strip())
        reaction_term_exists = int(f.readline().strip())

        # initial dummy node
        frnt_glob = Glob()
        back_glob = frnt_glob
        number_of_globs = 0

        # now the jumps
        while True:
            line = f.readline()
            if not line:
                break
            parts = [x.strip() for x in line.split(",")]
            jumps = int(parts[0])
            location = float(parts[1])
            value = float(parts[2])
            if jumps == -1:
                break
            for _ in range(jumps):
                g = Glob(location, value)
                g.prev = back_glob
                back_glob.next = g
                back_glob = g
                number_of_globs += 1

    # drop the dummy
    frnt_glob = frnt_glob.next
    if frnt_glob:
        frnt_glob.prev = None

    params = {
        "left_end_exists": int(le_exists),
        "left_end": float(le),
        "left_symmetric": int(le_sym),
        "rite_end_exists": int(re_exists),
        "rite_end": float(re),
        "rite_symmetric": int(re_sym),
        "alpha": alpha,
        "time_step": time_step,
        "reaction_term_exists": reaction_term_exists,
        "number_of_globs": number_of_globs,
    }
    return frnt_glob, back_glob, params
