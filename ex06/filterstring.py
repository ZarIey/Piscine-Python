import sys as check
from ft_filter import ft_filter


def main():
    assert len(check.argv) == 3, "Expected two arguments: a string and an integer."
    S = check.argv[1]
    splited_list = S.split()
    N = int(check.argv[2])
    sorted_list = list(ft_filter(lambda x: len(x) > N, splited_list))
    print(sorted_list)


if __name__ == "__main__":

    # print(ft_filter.__doc__)

    try:
        main()
    except AssertionError as e:
        print("Assertion error: ", e)
        check.exit()
    except KeyboardInterrupt:
        print("Arret du programme")
