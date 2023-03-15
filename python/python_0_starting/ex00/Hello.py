ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"

list_tuple = list(ft_tuple)
list_tuple[1] = "France!"
ft_tuple = tuple(list_tuple)

ft_set.remove("tutu!")
ft_set.add("Nice!")

dict_pers = {"Hello":  "42Nice!"}
ft_dict = dict_pers

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
