
def all_thing_is_obj(object: any) -> int:
	if type(object) == list:
		print("List :", type(object))
	elif type(object) == tuple:
		print("Tuple :", type(object))
	elif type(object) == set:
		print("Set :", type(object))
	elif type(object) == dict:
		print("Dict :", type(object))
	elif type(object) == str:
		print(object, "is in the kitchen", type(object))
	else:
		print("Type not found")
	return 42

# ------------------- test.py --------------------------

# from Find_my_type import all_thing_is_obj

# ft_list = ["Hello", "tata!"]
# ft_tuple = ("Hello", "toto")
# ft_set = {"Hello", "tutu!"}
# ft_dict = {"Hello" : "titi!"}

# all_thing_is_obj(ft_list)
# all_thing_is_obj(ft_tuple)
# all_thing_is_obj(ft_set)
# all_thing_is_obj(ft_dict)
# all_thing_is_obj("Brian")
# print(all_thing_is_obj(10))