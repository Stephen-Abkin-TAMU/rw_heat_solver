from pathlib import Path

def main():
    print("Welcome to the Gradient Random Walk set-up")

    out_name = input("Enter a filename to create: ").strip()
    out_path = Path(out_name)
    if out_path.exists():
        resp = input(f"WARNING: {out_name} exists. Overwrite? [y/n]: ").lower()
        if resp not in ("y", "yes"):
            print("ABORT.")
            return

    # domain type: 1 finite, 2 semi-infinite, 3 infinite
    print("Is the domain of this set-up:")
    print(" 1) Finite")
    print(" 2) Semi-Infinite")
    print(" 3) Infinite")
    domain_type = int(input("Please enter 1, 2 or 3: "))

    left_end_exists = 0
    rite_end_exists = 0
    left_end = 0.0
    rite_end = 0.0
    left_sym = 1
    rite_sym = 1

    def get_end(which):
        end = float(input(f" Enter location of the {which} end: "))
        print("Is the reflection:")
        print("  1) Dirichlet (symmetric)")
        print("  2) Newmann (anti-symmetric)")
        sym = int(input("Please enter 1 or 2: "))
        symmetric = 1 if sym == 1 else 0
        return end, symmetric

    if domain_type == 1:  # finite
        left_end_exists = 1
        left_end, left_sym = get_end("LEFT")
        rite_end_exists = 1
        rite_end, rite_sym = get_end("RIGHT")
    elif domain_type == 2:  # semi
        side = int(input("Would you like to define: 1) LEFT  or  2) RIGHT ? "))
        if side == 1:
            left_end_exists = 1
            left_end, left_sym = get_end("LEFT")
        else:
            rite_end_exists = 1
            rite_end, rite_sym = get_end("RIGHT")
    else:
        # infinite -> no ends
        pass

    alpha = float(input("Enter Diffusivity constant (alpha): "))
    time_step = float(input("Enter Time Step: "))
    jump_value = float(input("Enter value for the jumps (this is 'value' in the file): "))

    # reaction?
    reaction_term_exists = 0
    resp = input("Is there a reaction term in this run [y/n]? ").lower()
    if resp in ("y", "yes"):
        print("Is the reaction term:\n 1) Explicit (formula is known)\n 2) Implicit (computed numerically)")
        reaction_term_exists = int(input("Please enter 1 or 2: "))

    # now write the file exactly as the C did
    with out_path.open("w") as f:
        # line 1: left
        f.write(f"{left_end_exists}, {left_end}, {left_sym}\n")
        # line 2: right
        f.write(f"{rite_end_exists}, {rite_end}, {rite_sym}\n")
        # line 3: alpha
        f.write(f"{alpha}\n")
        # line 4: time_step
        f.write(f"{time_step}\n")
        # line 5: reaction term flag
        f.write(f"{reaction_term_exists}\n")

        # now the jump locations loop
        i = 1
        location = 0.0
        while True:
            location = float(input(f"Enter location of jump {i} (-9999 to exit): "))
            if location <= -9998:  # exit
                break
            jumps = int(input("How many at this location? "))
            # write: jumps, location, value
            f.write(f"{jumps}, {location}, {jump_value}\n")
            i += 1

        # final sentinel
        f.write(f"-1, 0.0, 0\n")

    print(f"Initialization complete. Wrote {out_name}")

if __name__ == "__main__":
    main()
