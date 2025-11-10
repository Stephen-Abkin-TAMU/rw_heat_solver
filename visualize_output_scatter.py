# visualize_output_scatter.py
# ------------------------------------------------------------------
# Purpose:
#   Show individual globs (walker positions) as discrete points.
#   Optionally overlay a best-fit or smoothed trend line.
#
# Visual interpretation:
#   - Blue dots = each random-walk bin / glob (the real data)
#   - Orange line = local-averaged trend showing diffusion behavior
# ------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

def main():
    fname = input("Enter output filename to visualize [sample_output.txt]: ").strip()
    if fname == "":
        fname = "sample_output.txt"

    data = np.loadtxt(fname, delimiter=",")

    # handle the case of a single line in the file
    if data.ndim == 1:
        data = np.expand_dims(data, axis=0)

    x = data[:, 0]
    u = data[:, 1]

    # scatter the raw data
    plt.scatter(x, u, s=25, color="C0", alpha=0.8, label="individual globs (raw data)")

    # --- smoothing, but only if we have enough points ---
    if len(u) > 3:          # arbitrary cutoff; 3+ is enough to smooth
        window = min(11, len(u))   # don't let window be bigger than the data
        kernel = np.ones(window) / window
        u_smooth = np.convolve(u, kernel, mode="same")
        plt.plot(x, u_smooth, "C1-", linewidth=2, label="smoothed trend")
    else:
        # with only 1–2 points, just connect them or do nothing
        plt.plot(x, u, "C1-", linewidth=2, label="trend (no smoothing)")

    plt.xlabel("x position")
    plt.ylabel("u(x)")
    plt.title(f"Random-walk globs and smoothed field from {fname}")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()