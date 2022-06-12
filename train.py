import argparse
import sys
import wandb

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--arg", required=True)
    p.add_argument("--flag", action="store_true")
    args = p.parse_args()

    wandb.init(project="debugging-args_no_boolean_flags", config=args)
    print("flag is true" if args.flag else "flag is false")
    wandb.log({"val1": 3.14})

if __name__ == "__main__":
    print("Got command line:")
    print(" ".join(sys.argv))
    main()
    print("Done.")
