from rw_header import Glob

def Add_a_glob(frnt_glob, curr_glob, back_glob):
    temp_glob = Glob(curr_glob.location, curr_glob.value)
    # insert right after curr_glob
    nxt = curr_glob.next
    curr_glob.next = temp_glob
    temp_glob.prev = curr_glob
    temp_glob.next = nxt
    if nxt is not None:
        nxt.prev = temp_glob
    else:
        back_glob = temp_glob
    return temp_glob, back_glob
