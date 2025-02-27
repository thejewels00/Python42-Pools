ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"

temp = list(ft_tuple)
temp[1] = "Morocco!"
ft_tuple = tuple(temp)

ft_set.discard("tutu!")
ft_set.add("Ben guerir!")

ft_dict["Hello"] = "1337!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)