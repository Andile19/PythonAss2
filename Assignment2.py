#   Create an empty list called my_list.
my_list=[]
#   Append the numbers 10, 20, 30, and 40 to the list.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#   Insert the number 15 at position 1.
my_list.insert(1, 15)
#   Extend the list by adding the numbers 50, 60, and 70.
my_list.extend([50, 60, 70])
#   Remove the last element from my_list.
my_list.pop()
#   Sort my_list.
my_list.sort()
#   Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("Index of 30 is: ", index_of_30)
