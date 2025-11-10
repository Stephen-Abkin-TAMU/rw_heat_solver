def Compute_U(frnt_glob, bin_width=0.5):
    """
    Rebuild a field u(x) from the list of globs.
    - bins the x-axis
    - averages values per bin (not just sum)
    - fills empty bins with the previous value to make the plot smooth
    """
    # 1) collect all globs into a list so we can scan min/max
    globs = []
    curr = frnt_glob
    while curr is not None:
        globs.append((curr.location, curr.value))
        curr = curr.next

    if not globs:
        return []

    # 2) find domain
    xs = [g[0] for g in globs]
    xmin, xmax = min(xs), max(xs)

    # 3) make bins
    n_bins = int((xmax - xmin) / bin_width) + 1
    bin_sums   = [0.0] * n_bins
    bin_counts = [0]   * n_bins

    # 4) deposit globs into bins
    for x, v in globs:
        idx = int((x - xmin) / bin_width)
        if 0 <= idx < n_bins:
            bin_sums[idx] += v
            bin_counts[idx] += 1

    # 5) build (x, u) list, averaging, and filling empties
    field = []
    last_u = 0.0
    for i in range(n_bins):
        x_center = xmin + i * bin_width
        if bin_counts[i] > 0:
            u = bin_sums[i] / bin_counts[i]   # <-- average instead of sum
            last_u = u
        else:
            u = last_u                        # <-- carry forward to avoid jagged gaps
        field.append((x_center, u))

    return field
