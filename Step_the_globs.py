from rw_header import (
    left_end_exists, rite_end_exists,
    left_end, rite_end,
    left_symmetric, rite_symmetric,
)
from Step import Step

def Step_the_globs(frnt_glob):
    curr_glob = frnt_glob
    while curr_glob is not None:
        # 1) move
        curr_glob.location += Step()

        # 2) reflect back into domain if needed
        reflected = curr_glob.location
        while ((left_end_exists and reflected < left_end) or
               (rite_end_exists and reflected > rite_end)):
            if left_end_exists and reflected < left_end:
                reflected = 2.0 * left_end - reflected
                if left_symmetric == 0:
                    curr_glob.value = -curr_glob.value
            if rite_end_exists and reflected > rite_end:
                reflected = 2.0 * rite_end - reflected
                if rite_symmetric == 0:
                    curr_glob.value = -curr_glob.value

        curr_glob.location = reflected
        curr_glob = curr_glob.next

    return frnt_glob
