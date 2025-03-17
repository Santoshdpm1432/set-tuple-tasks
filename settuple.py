# tuple_1 = (1,2,3,3,4,5,6,'santosh','rajesh','ashok')
# print(tuple_1)

# Tuples with Built-in Functions:

# len() function:
# length = len(my_tuple)

# tuple_1 = (1,2,3,3,4,5,6,'santosh','rajesh','ashok')
# length = len(tuple_1)
# print(tuple_1)
# print(length)

#  count() method:
# Returns the number of occurrences of a specified value.

# occurrences = my_tuple.count(value)

# tuple_1 = (1,2,3,3,1,1,1,14,5,6,'santosh','rajesh','ashok')
# countable = tuple_1 . count(1)
# print(countable)
# print(tuple_1)

# index() method:
# Returns the index of the first occurrence of a specified value.

# Syntax:
# index = my_tuple.index(value)

# tuple_1 = (1,2,3,3,1,1,1,14,5,6,'santosh','rajesh','ashok')
# print(tuple_1 . index('santosh'))

# Tuple Operations:

# Concatenation:
# Combine two tuples to create a new tuple.

# new_tuple = tuple1 + tuple2

# tuple1 = (1,2,3,4,5)
# tuple2 = ("santosh","ashok","nagaprasad")
# result = tuple1 + tuple2
# print(result)


# Repetition:
# Repeat a tuple for a specified number of times.

# Syntax:
# new_tuple = my_tuple * n

# tuple1 = (1,2,3,4,5)
# result = tuple1 * 3
# print(result)

# Membership Test:
# Check if an element is present in the tuple.

# Syntax:
# is_present = element in my_tuple

# tuple1 = ('santosh','ashok','nagaprasad','rajasekhar')
# result = 'santosh' in tuple1
# print(result)

# task_1

# Write a program that creates a tuple containing three
# elements: your name, your age, and your favorite color. Then print the

# tuple1 = ("name = santosh","age = 25", "favrite colour = black")
# print(tuple1)


# task_2

# Access Tuple Elements: Write a program that creates a tuple containing the
# days of the week. Then, print the third element of the tuple.

# days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
# print(f"third day of the week is : {days_of_week[2]}")

# task_3

# Tuple Concatenation: Write a program that creates two tuples, one
# containing odd numbers from 1 to 5 and another containing even numbers
# from 2 to 6. Concatenate these two tuples and print the result

# tuple1 = (1,3,5)
# tuple2 = (2,4,6)
# result = tuple1 + tuple2
# print(result)

# task_4

# Tuple Unpacking: Write a program that defines a tuple containing the
# dimensions of a rectangle (length and width). Then, unpack this tuple into
# two variables and calculate the area of the rectangle.


# rectangle = (10,60)
# lenght , width = rectangle
# area = lenght * width
# print(area)

# task_5

# Write a program that checks if a given element
# exists in a tuple.

# tuple1 = ('santosh', 'ashok', 'nagaprasad','rajasekhar')
# result = 'santosh' in tuple1
# print(result)


# sets////////////////////////////////////////////////////////////////////////

# set_1 = {"python",1,2,3,"vasu",5.7,(1,2)}
# print(set_1)
# list_1 = [1,2,3,]
# set_2= set(list_1)
# print(set_2)

# set_1 = {"santosh",1,2,3,"ashok",5.7,(1,2)}
# set_1.add("kumar")
# print(set_1)

# set_1 = {"santosh",1,2,3,"ashok",5.7,(1,2)}
# set_1.clear()
# print(set_1)

# set_1 = {"santosh",1,2,3,"ashok",5.7,(1,2)}
# obj = set_1.copy()
# print(obj)

# set_1 = {"santosh",1,2,3,"ashok",5.7,(1,2)}
# set_1.pop()
# print(set_1)

# set_1 = {"santosh",11,24,3,"kumar",5.7,(1,2),"nagaprasad"}

# set_2 = {"rajasekhar","mohan","anil","sneha"}
# set_2.update(set_1)
# # print(set_2)
# set_1.remove(("santosh"))
# print(set_1)

# set_1 = {1,2,3,4}
# set_2 = {3,4,5,6,7}
# set_3 = set_1.union(set_2)
# print(set_3)

# set_1 = {1,2,3,4,7}
# set_2 = {3,4,5,6,7}
# set_3 = set_1.intersection(set_2)
# print(set_3)

# set_1 = {1,2,3,4}
# set_2 = {3,4,5,6,7}
# set_3 = set_1.symmetric_difference(set_2)
# print(set_3)

# set_1 = {1,2,3,4}
# set_2 = {3,4,5,6,7}
# set_3 = set_1.difference(set_2)
# print(set_3)

# prices= {99,22,55,88,89}
# prices_2 = {100,25,55,44,22,99}
# compare = prices.difference(prices_2)
# print(compare)

# prices= {99,22,55,88,89}
# prices_2 = {100,25,44,}
# print(prices_2.isdisjoint(prices))

# set_1 = {1,2,3,4}
# set_2 = {1,2}
# print(set_1.issuperset(set_2))
# print(set_2.issubset(set_1))

# prices= {99,22,55,}
# prices_2 = {100,99,22,55}
# print(prices_2.issuperset(prices))
# print(prices.issubset(prices_2))

# set_1 = {1,2,3,4,5}
# set_1.add("vasu")
# print(set_1)
# set_2 = frozenset(set_1)
# print(set_2)


# task_1

# Write Python code to find and print the intersection of the following two sets:
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# Your code here
# Output should be: {4, 5}

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1.intersection(set2))

# task_2

# Write Python code to find and print the union of the following two sets:
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# Your code here
# Output should be: {1, 2, 3, 4, 5, 6, 7, 8}

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1.union(set2))


# task_3

# Write Python code to find and print the elements present in set1 but not in
# set2 :
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# Your code here

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1.difference(set2))


# task_4

# Write Python code to find and print the symmetric difference of the following
# two sets:
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# Your code here
# Output should be: {1, 2, 3, 6, 7, 8}

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1.symmetric_difference(set2))
total_cost = 0
items = [("Apple",    99), ("Banana",     99), ("Milk",     49)]
print("items        price")
print("-------------------")
for items,price in items :
    print(f"{items} {price}")
    total_cost += price
print("--------------------")
print(f"your total  {total_cost}")