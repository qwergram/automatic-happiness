import os
import sys

def main(target):
    os.system("ls " + target)


if __name__ == "__main__":
    target = sys.argv[1]
    main(target)
