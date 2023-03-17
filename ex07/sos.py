import sys as check


def main():
    morse = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--.."
    }
    x = len(check.argv) 
    assert x > 3, "the arguments are bad"
    
    catch = check.argv[2]
    print(catch)
    for i in range(len(catch)):
        if catch[i].isupper():
            catch[i].toupper()
    print(catch)


if __name__ == "__main__":

    try:
        main()
    except AssertionError as e:
        print("Assertion error:", e)
        check.exit()
    except KeyboardInterrupt:
        print("Arret du programme")
