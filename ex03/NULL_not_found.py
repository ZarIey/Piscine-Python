def NULL_not_found(object: any) -> int:
    if type(object) == type(None):
        print("Nothing: ", object, type(object))
    elif object != object:
        print("Cheese:", object, type(object))
    elif object == 0 and type(object) == int:
        print("Zero:", object, type(object))
    elif object == "":
        print("Empty:", object, type(object))
    elif type(object) == bool:
        print("Fake:", object, type(object))
    else:
        print("Type not found")
        return 1
    return 0

# from NULL_not_found import NULL_not_found

# Nothing = None
# Garlic = float("NaN")
# Zero = 0
# Empty = ""
# Fake = False

# NULL_not_found(Nothing)
# NULL_not_found(Garlic)
# NULL_not_found(Zero)
# NULL_not_found(Empty)
# NULL_not_found(Fake)
# print(NULL_not_found("Brian"))

# $>python test_my_ex02.py | cat -e
# Nothing: None <class 'NoneType'>$
# Cheese: nan <class 'float'>$
# Zero: 0 <class 'int'>$
# Empty: <class 'str'>$
# Fake: False <class 'bool'>$
# Type not Found$
# 1$
# $>
