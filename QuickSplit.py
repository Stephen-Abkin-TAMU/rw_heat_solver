from Swap import Swap

def QuickSplit(frnt_glob, back_glob):
    lp = frnt_glob
    rp = back_glob

    while lp is not rp:
        while frnt_glob.location >= lp.location and lp is not rp:
            lp = lp.next
        while frnt_glob.location < rp.location and lp is not rp:
            rp = rp.prev
        if lp is not rp:
            Swap(lp, rp)

    if (lp is back_glob) and (frnt_glob.location > back_glob.location):
        Swap(frnt_glob, back_glob)
        rp = back_glob
    else:
        Swap(frnt_glob, lp.prev)
        rp = lp.prev
    return rp
