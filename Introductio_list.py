"""Simple making list """
# name = ['vruti', 'mitul', ' jheel']
# print("Hello i am "+name[0].title()+".")

""" Changing , adding and remove elements """

# >>> Change elements in list
# name[1] = 'vishva'
# print(name)
# name[0] = 'lavleen'.title()
# print(name)

# >>> adding a element in list using append() method
# name.append('vishva')
# print(name)
#
# value = input("add your name = ")
# name.append(value.title())
# print(name)

# >>> using insert() method

# name.insert(0, 'vishva')
# print(name)
# print(name[0])

# remove elements from a list
name = ['vruti', 'mitul', ' jheel', 'lavleen']
# print(name)
# >>> delete statement
# del name[1]
# print(name)

# >>> pop method
# boys= ['Arvind', 'yash', 'arihnat', 'aayush']
# boys_list = name.pop(1)
# boys.append(boys_list)
# print(name)
# print(boys)

# >>> remove() method
# name.remove('vruti')
# print(name)

""" Organizing a list"""
boys= ['arvind', 'yash', 'arihnat', 'aayush', 'mitul']

# >>> Parmanntly Sorting a list using sort() method
# print(boys)
# boys.sort(reverse=True)
# print(boys)

# >>> sorting a list Temporarily with the sorted() list
print(sorted(boys))
print(boys)
boys.reverse()
print(boys)

# finding the length of list
print(len(boys))








