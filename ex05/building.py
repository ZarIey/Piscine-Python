import sys as check


def call_arg_to_input() -> str:
    print("What is the text to count ?")
    catch = check.stdin.readline()
    return catch


def main():
    x = len(check.argv)
    if x == 1:
        catch = call_arg_to_input()
    elif x == 2:
        catch = check.argv[1]
    assert x <= 2, "more than one argument are provided"
    cnt_upper, cnt_lower, cnt_digit, cnt_space, cnt_punct = 0, 0, 0, 0, 0
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    for i in range(len(catch)):
        for j in range(len(punctuation)):
            if punctuation[j] == catch[i]:
                cnt_punct += 1
        if catch[i].isspace():
            cnt_space += 1
        if catch[i].isupper():
            cnt_upper += 1
        if catch[i].isdigit():
            cnt_digit += 1
        if catch[i].islower():
            cnt_lower += 1
    cnt_total = cnt_digit + cnt_lower + cnt_punct + cnt_upper + cnt_space
    print("The text contain", cnt_total, "characters:")
    print(cnt_upper, "upper letters")
    print(cnt_lower, "lower letters")
    print(cnt_punct, "punctuations marks")
    print(cnt_space, "spaces")
    print(cnt_digit, "digits")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("Assertion error: ", e)
        check.exit()
    except KeyboardInterrupt:
        print("Arret du programme")
