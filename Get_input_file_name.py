from pathlib import Path

def Get_input_file_name():
    name = input("\nEnter input file name: ").strip()
    if not Path(name).exists():
        print("\nERROR: File does not exist.\n")
        raise SystemExit(1)
    return name