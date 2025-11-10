from pathlib import Path

def Get_output_file_name():
    name = input("\nEnter filename to OUTPUT results: ").strip()
    p = Path(name)
    if p.exists():
        resp = input("WARNING: Output file exists. Do you wish to overwrite [y/n]: ")
        if resp not in ("y", "Y"):
            print("\nGood-bye\n")
            raise SystemExit(0)
    return name
