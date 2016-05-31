import os
import io
import sys


def get_git_ignore(target):
    try:
        with io.open(os.path.join(target, '.gitignore')) as f:
            gitignore = [ignore_this.strip() for ignore_this in f.readlines()]
        return gitignore
    except IOError:
        return []


def ls(target):
    return os.listdir(target)


def main(target):
    print(ls(target))
    gitignore = get_git_ignore(target)
    print(gitignore)


if __name__ == "__main__":
    target = sys.argv[1]
    main(target)
