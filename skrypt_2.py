#!/usr/bin/env python3
import sys

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python script2.py [success|fail]")
        sys.exit(1)          # no param ⇒ fail

    arg = sys.argv[1].lower()

    if arg == "success":
        print("Operation successful for script 2")
        sys.exit(0)          # exit code 0 = OK
    elif arg == "fail":
        raise RuntimeError("Forced error for script 2")  # Exception ⇒ code ≠ 0
    else:
        print(f"Nieznany parametr: {arg}")
        sys.exit(2)          # code 2 = wrong param

if __name__ == "__main__":
    main()