#slicing lets you access a subset of a sequences itesm with minimal effort.
#simplist uses for slicing are the built-in types list, str, and bytes
#slicing implements __getitem__ , __setitem__ methods

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print('First Four', a[:4])
print('Last Four', a[-4:])
print('Middle Two', a[3:-3])

assert a[:5] == a[0:5] #assert throws an error if the condition is false

#b = a[12] #will throw an error because 12 is out of range

b = a[20:20] #will not throw an error because slicing deals with bounndry issues
b

#the results of slicing is a whole new list, references to the objects from the original list are maintained. 
#modifying a sliced list wony change the original list

b = a[:4]
b[1] = 99 #this alters list b but does not affect the a list

#leaving out starting and end indexes will copy the who list
c = a[:]
c == a and c is not a
a is a 


 #if you assign a list to a new variable with no indexes you make a new reference to
#to that list but you dont create a new list in memory
d = a

d == a and d is a #d is A!!!!!!!!!!!!!!!!

a[:] = [100, 200, 300]
#even after you change a d is a because its a reference
d is a

#however if i were to just assign, a the same would not be true
a = ['giggidy', 'giggidy', 'goo']
d is a

#python has a special syntax for the stride of a slice in the form somelies[start:end:stried]
#this lets you take every nth item of a list 
#i.e.
a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

odds = a[::2]
evens = a[1::2]

#strides can alow you to reverse a string (take this byte string)
x = b'mongoose'
y = x[::-1] 

#works for byte strings and ASCII but not unicode or UTF-8

#List Comprehension
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a] #list comprehension for loop

#you can also use maps like so
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = map(lambda x: x**2, a)
