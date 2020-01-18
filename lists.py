my_list1 = [1,2,3]                           # declaration of Simple list  
my_list = [1, "Hello", 2, "World", 2.56]    # Declaring list with string, int no., floating point no.

print(len(my_list))                         # using len() func. to find the length of list
                                
                                # indexing of lists

print(my_list[1])                           # to display an element of a list at given index no.

                                # slicing of lists

# to display the elements of a list starting from given index no. upto end (element at index no. given included)
print(my_list[1:])

# to display the elements of a list  from starting upto the given index no. (element at iindex no. given not included )
print(my_list[:3])

# to concatinate two lists
print(my_list1 + my_list)

# to save concatinated lists into a new list
new_list = my_list1 + my_list
print(new_list)

# to change element of a list just use the name of the list followed by yhe index no. equals to the new element
my_list[3] = 4
print(my_list)

# to add new element to list at the end of the list
my_list.append("Abhi")
my_list.append(56)
my_list.append(9.8)
print(my_list)

# to pop an element from the end of the list                remove commnets marks to run the prog.
# my_list.pop()
# popped_item = my_list.pop()
# print(my_list)
# print(popped_item)                                

# to pop an element from a particular index no.             remove commnets marks to run the prog.
# my_list.pop(2)
# popped_item = my_list.pop(2)
# print(my_list)
# print(popped_item)

# sorting and reversing of a list
list1 = [1,6,3,8,5,9]
list2 = ['a','g','e','v','r']
list1.sort()
list2.sort()
print(list1)        # sorted list 1
print(list2)        # sorted list 2

list1.reverse()
list2.reverse()
print(list1)        # reversed sorted list 1 
print(list2)        # reversed sorted list 2
