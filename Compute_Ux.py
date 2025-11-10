from Get_slope import Get_slope

def Compute_Ux(frnt_grid, frnt_glob):
    """
    Fill in U, Ux, Uxx on the glob list.
    The original C code computed derivatives from neighboring points
    use Get_slope() helper in the same way in Python.
    """
    curr = frnt_glob
    while curr is not None:
        # in the original code, U was already the bin total;
        # in this port, we'll just mirror the "value" onto U
        curr.U = curr.value

        # first derivative
        curr.Ux = Get_slope(curr, 1)

        # second derivative
        curr.Uxx = Get_slope(curr, 2)

        curr = curr.next
