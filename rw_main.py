from Get_input import Get_input
from Step_the_globs import Step_the_globs
from Reaction import Reaction
from Compute_U import Compute_U

def main():
    # 1) read input
    input_name = input("Enter input file name [linear_input.txt]: ").strip() or "linear_input.txt"
    output_name = input("Enter filename to OUTPUT results [linear_output.txt]: ").strip() or "linear_output.txt"

    frnt_glob, back_glob, params = Get_input(input_name)

    max_time = float(input("Enter time level to compute (e.g. 0.01): "))
    time_step = params["time_step"]
    reaction_term_exists = params["reaction_term_exists"]

    curr_time = time_step
    while curr_time <= max_time and max_time != 0.0:
        print(f"t = {curr_time:.3f} ({params['number_of_globs']} globs)")
        frnt_glob = Step_the_globs(frnt_glob)
        back_glob = frnt_glob # list head stays the same in python port

        # reaction, if any
        if reaction_term_exists:
            frnt_glob = Reaction(frnt_glob, back_glob, curr_time, reaction_term_exists)

        curr_time += time_step

    # 2) reconstruct and write
    field = Compute_U(frnt_glob, bin_width=0.02)

    with open(output_name, "w") as f:
        for x, u in field:
            f.write(f"{x}, {u}\n")

    print(f"Simulation complete. Results written to: {output_name}")

if __name__ == "__main__":
    main()
