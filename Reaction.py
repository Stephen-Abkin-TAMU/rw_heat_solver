from Add_a_glob import Add_a_glob
from Nuke_a_glob import Nuke_a_glob
from E_reaction import E_reaction
from N_reaction import N_reaction
from rw_header import time_step, drand48
from Compute_Ux import Compute_Ux  

def Reaction(frnt_glob, back_glob, frnt_grid, t, reaction_term_exists):
    curr_glob = frnt_glob
    while curr_glob is not None:
        if reaction_term_exists == 1:
            critical_value = time_step * E_reaction(t, curr_glob.location)
        elif reaction_term_exists == 2:
            critical_value = time_step * N_reaction(curr_glob.U, curr_glob.Ux, curr_glob.Uxx)
        else:
            critical_value = 0.0

        if abs(critical_value) > drand48():
            if critical_value > 0.0:
                # add a glob
                new_glob, back_glob = Add_a_glob(frnt_glob, curr_glob, back_glob)
                curr_glob = new_glob
            else:
                # nuke
                frnt_glob, curr_glob, back_glob = Nuke_a_glob(frnt_glob, curr_glob, back_glob)
        if curr_glob is not None:
            curr_glob = curr_glob.next

    return frnt_glob
