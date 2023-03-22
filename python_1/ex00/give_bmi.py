import sys as check


def parsing_bmi(height, weight):
    '''parsing for bmi'''
    if type(height) != list or type(weight) != list:
        print("Error: arguments are not list ")
        check.exit()
    if (len(height) != len(weight)):
        print("Error: lists are not the same size")
        check.exit()
    for i, (h, w) in enumerate(zip(height, weight)):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            print("Error: lists contain a bad type")
            check.exit()


def parsing_apply(bmi, limit):
    '''parsing for apply'''
    if type(bmi) != list:
        print("Error: iterable provided is not a list")
        check.exit()
    for i in range(len(bmi)):
        if type(bmi[i]) != int and type(bmi[i]) != float:
            print("List contain a bad type")
            check.exit()
    if type(limit) != int:
        print("Error: limit is not an int")
        check.exit()


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    '''fonction for caculate the bmi'''
    parsing_bmi(height, weight)
    imc = [weight[i] / (height[i] ** 2) for i in range(len(height))]
    return imc


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''aplly a limit to the bmi'''
    parsing_apply(bmi, limit)
    bool1 = list(map(lambda x: x > limit, bmi))
    return bool1
