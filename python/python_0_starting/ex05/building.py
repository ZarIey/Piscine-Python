import sys as check

def string_punct(str) -> int:
    count = 0
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' + '\n' + '\v' + '\t'
    for i in range(len(punctuation)):
        for j in range(len(str)):
            if str[j] == punctuation[i]:
                count += 1
    return count

def string_upper(str) -> int:
    count = 0
    for i in range(len(str)):
        if str[i].isupper():
                count += 1
    return count

def string_space(str) -> int:
    count = 0
    for i in range(len(str)):
        if str[i].isspace() or str[i] == '\n' or str[i] == '\v' or str[i] ==  '\t':
                count += 1
    return count

def string_digit(str) -> int:
    count = 0
    for i in range(len(str)):
        if str[i].isdigit():
                count += 1
    return count

def call_arg_to_input() -> str:
	catch = input("What is the text to count ?\n")
	return catch

def main():
    if len(check.argv) == 1:
        catch = call_arg_to_input()
    for i in range(len(catch)):
        count_punct = string_punct(catch)
        count_upper = string_upper(catch)
        count_space = string_space(catch)
        count_digit = string_digit(catch)
    print(count_upper, "upper letters")
    print(count_punct, "punctuations marks")
    print(count_space, "spaces")
    print(count_digit, "digits")
	
if __name__ == "__main__":
    main()