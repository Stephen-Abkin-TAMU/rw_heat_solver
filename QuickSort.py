from QuickSplit import QuickSplit

def QuickSort(frnt_glob, back_glob):
    if frnt_glob is not back_glob:
        split_glob = QuickSplit(frnt_glob, back_glob)
        if split_glob is not frnt_glob:
            QuickSort(frnt_glob, split_glob.prev)
        if split_glob is not back_glob:
            QuickSort(split_glob.next, back_glob)
    return frnt_glob
