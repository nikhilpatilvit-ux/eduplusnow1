#nikhil patil

#1. Create a list of 10 integers and print all even numbers from the list.
# l1=[1,2,3,4,5,6,7,8,9,10]
# for i in l1:
#     if(i%2==0):
#         print(i)

#2. Write a Python program to find the maximum and minimum value in a list.
# l2=[10,20,30,40,50]
# print(max(l2))
# print(min(l2))

#3. Create a list of student names and sort them alphabetically.
# l3=["tom","alex","ram","max"]
# print(sorted(l3))

#4. Reverse a given list without using the reverse() function.
# l4=[1,2,3,4,5]
# print(l4[::-1])

#5. Remove duplicate elements from a list.
# l5=[1,1,2,2,3,3,4,4,5,5]
# res=set(l5)
# res1=list(res)
# print(res1)

#6. Merge two lists into a single list.
# l=[1,2,3,4,5]
# l6=[6,7,8]
# res=l+l6
# print(res)

#7. Find the second largest number in a list.
# l7=[10,20,30,40,50]
# res=sorted(l7,reverse=True)
# print(res[1])

#8. Count how many times a specific element appears in a list.
# l8=[1,1,2,2,3,3,4,4,5]
# count=0
# res=int(input("Enter number:"))
# for i in l8:
#     if(res==i):
#         count=count+1
# print(count)

#9. Create a nested list and access specific elements from it.
# l9=[1,2,[3,4],5]
# print(l9[2][0])

#10. Convert a list of strings into uppercase using a loop.
# l10=["alex","max","tom"]
# for i in l10:
#     print(i.upper())

#11. Create a set of five city names and print the set.
# s11={"pune","nashik","dhule","mumbai","nagar"}
# print(s11)

#12. Add multiple elements into a set using update().
# s12={1,2}
# s12.update(["pune","nagar"])
# print(s12)

#13. Remove an element from a set using remove() and discard().
# s13={1,2,3,4,5}
# s13.remove(1)
# print(s13)
# s13.discard(2)
# print(s13)

#14. Find the union of two sets.
# s={1,2,3,4}
# s14={3,4,5,6}
# res=s | s14
# print(res)

#15. Find the intersection of two sets.
# s={1,2,3,4}
# s15={3,4,5,6}
# res=s & s15
# print(res)

#16. Find the difference between two sets.
# s={1,2,3,4}
# s15={3,4,5,6}
# res=s - s15
# print(res)

#17. Check whether a particular element exists in a set.
# s17={1,2,"nagar"}
# print("nagar" in s17)

#18. Convert a list with duplicate values into a set.
# l18=[1,1,2,2,3,3]
# res=set(l18)
# print(res)

#19. Create a frozen set and explain why elements cannot be modified.
# s19=frozenset(["a","a","b","c"])
# print(s19)
# as frozenset is immutable it cant be modified.

#20. Perform symmetric difference operation on two sets.
# s={1,2,3,4}
# s15={3,4,5,6}
# res=s ^ s15
# print(res)

#21. Create a tuple containing employee details and print each element.
# emp=(1,"max","IT","pune")
# for i in emp:
#     print(i)

#22. Create a tuple with mixed data types.
# t22=(1,"max",3.5,True)
# print(t22)

#23. Find the length of a tuple.
# t23=(1,2,3,4,5)
# print(len(t23))

#24. Count the occurrence of a particular element in a tuple.
# t24=(1,1,2,2,3,3,4,5)
# res=int(input("enter number:"))
# count=0
# for i in t24:
#     if (res==i):
#         count=count+1
# print(count) 

#25. Find the index position of an element in a tuple.
# t25=(1,2,3,4,5)
# print(t25.index(2))

#26. Convert a tuple into a list and modify its elements.
# t26=(1,2,3,4,5)
# res=list(t26)
# res[2]=40
# res1=tuple(res)
# print(res1)

#27. Concatenate two tuples into one tuple.
# t=(1,2,3)
# t27=(4,5,6)
# sum=t+t27
# print(sum)

#28. Create a single-element tuple correctly.
# t28=(1,)
# print(t28)

#29. Perform tuple unpacking with multiple variables.
# t29=(1,"nagar",2.5)
# a,b,c=t29
# print(a)
# print(b)
# print(c)

#30. Create a nested tuple and access inner elements.
# t30=(1,2,(3,4),5)
# print(t30[2][0])

#31. Create a dictionary with student names and marks.
# d31={"alex":81,"max":90,"ram":92}
# print(d31)

#32. Add a new key-value pair into an existing dictionary.
# d32={"alex":81,"max":90,"ram":92}
# d32["shyam"]=72
# print(d32)

#33. Update the value of an existing key in a dictionary.
# d33={"alex":81,"max":90,"ram":92}
# d33["alex"]=100
# print(d33)

#34. Delete a key from a dictionary using pop() and del.
# d34={"alex":81,"max":90,"ram":92}
# del d34["alex"]
# print(d34)
# d34.pop("max")
# print(d34)

#35. Print all keys, values, and items from a dictionary.
# d35={"alex":81,"max":90,"ram":92}
# for i in d35.keys():
#     print(i)
# for j in d35.values():
#     print(j)
# for key,value in d35.items():
#     print(key,value)    

#36. Check whether a particular key exists in a dictionary.
# d36={"alex":81,"max":90,"ram":92}
# print("alex" in d36)

#37. Merge two dictionaries into one dictionary.
# students={
# 36:{"alex":81,"max":90,"ram":92},
# 37:{"alex":81,"max":90,"ram":92}
# }
# print(students)


#38. Create a dictionary using dictionary comprehension.
# d38={x:x**2 for x in range(1,5)}
# print(d38)

#39. Swap two numbers using assignment operators without a third variable.
# a=1
# b=2
# a+=1
# b-=1
# print(a)
# print(b)

#40. Write a Python program demonstrating arithmetic, comparison, logical, assignment, membership, and identity operators.
# a=1
# b=2
# s="ram"
# c=a+b
# print(c)
# d=a-b
# print(d)
# if(a>b):
#     print("true")
# elif(a<b):
#     print("false")
# elif(a>b)or(a<b):
#     print("something")
# else:
#     print("Stop")
# a+=1
# print(a)
# if("a" in s):
#     print("true") 
