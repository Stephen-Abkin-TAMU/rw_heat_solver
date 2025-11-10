def Sort_the_globs(frnt_glob):
    # dump to list
    arr = []
    curr = frnt_glob
    while curr is not None:
        arr.append(curr)
        curr = curr.next
    # sort
    arr.sort(key=lambda g: g.location)
    # re-link
    for i, g in enumerate(arr):
        g.prev = arr[i-1] if i > 0 else None
        g.next = arr[i+1] if i < len(arr)-1 else None
    return arr[0] if arr else None
