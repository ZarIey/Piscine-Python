import sys as check


def funct():
    if len(check.argv) == 1:
        check.exit()
    if len(check.argv) > 2:
        raise AssertionError(
            "AssertionError: more than one argument are provided")
    try:
        if int(check.argv[1]) % 2:
            print("I'm Odd.")
            check.exit()
        print("I'm Even.")
    except ValueError:
        raise AssertionError("AssertionError: argument is not an integer")


try:
    funct()
except AssertionError as e:
    print(e)
    exit()
except KeyboardInterrupt:
    print("Arret du programme")
