#lst = [1,2,3]
#my_str = "Vikas jangid"
#my_int = 8

#print(type(lst))  # <class 'list'>
#print(type(my_str))  # <class 'str'>    
#print(type(my_int))  # <class 'int'>\


from oops_proj import chatbook

user1 = chatbook()
print(user1.id)

chatbook.set_id(0)
user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)

user4 = chatbook()
print(user4.id)


#print(user1.get_name())
#user1.set_name("James Bond")
#print(user1.get_name())


#print(user1._chatbook__name)
#print(user1.__name)
#print(user1.name)


