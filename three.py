#nikhil patil
# 1. Create a tuple named 'fruits' containing five fruit names and print it.
# t1=("apple","orange","grapes","cherry","banana")
# print(t1)

# 2. Create a tuple with mixed data types (string, integer, float, boolean) and display each element using indexing.
# t2=("apple",1,2.5,True)
# print(t2[0])
# print(t2[1])
# print(t2[2])
# print(t2[3])

# 3. Create a nested tuple that stores a country name and its states as another tuple.
# t3=("India",("mh","mp","gj"))

# 4. Access the last element of a tuple using negative indexing.
# t4=(1,2,3,4,5,6,7)
# print(t4[-1])

# 5. Slice a tuple to print only the first three elements.
# t5=(1,2,3,4,5,6,7,8)
# print(t5[0:3:1])

# 6. Use len() to find the number of elements in a tuple named 'students'.
# students=("ram","shyam","seeta","geeta")
# print(len(students))

# 7. Use max() and min() to find the highest and lowest marks from a tuple of integers.
# t7=(40,50,66,78,98,81)
# print(max(t7))
# print(min(t7))

# 8. Use sum() to calculate the total sales from a tuple of daily sales data.
# sales=(150,200,250,300,400)
# print(sum(sales))

# 9. Sort a tuple of numbers in ascending order using sorted() and convert it back to a tuple.
# t9=(100,99,98,97,96,45,23)
# asc=tuple(sorted(t9))
# print(asc)

# 10. Sort a tuple of numbers in descending order using sorted() with reverse=True.
# t10=(1,2,3,4,5,6,7,8,89)
# desc=tuple(sorted(t10,reverse=True))
# print(desc)

# 11. Count how many times a specific value appears in a tuple using the count() method.
# t11=(1,2,3,2,4,5,2,6,2)
# print(t11.count(2))

# 12. Find the index of a specific element in a tuple using the index() method.
# t12=(1,2,3,4,5,6)
# print(t12.index(2))

# 13. Check if "Python" is present in a tuple using the 'in' keyword.
# t13=("apple","Python","bat")
# print("Python" in t13)

# 14. Check if "C++" is not present in a tuple using the 'not in' keyword.
# t14=("apple","Python","bat","C++")
# print("C++" not in t14)

# 15. Create a tuple from a range of numbers 1 to 10 using the tuple() and range() functions.
# t15=tuple(range(1,11))
# print(t15)

# 16. Use any() on a tuple of boolean values to check if at least one element is True.
# t16=("True","False","True")
# print(any(t16))

# 17. Use all() on a tuple of boolean values to check if all elements are True.
# t17=("True","True")
# print(all(t17))

# 18. Concatenate two tuples representing first names and last names.
# t18=("nikhil","krishna","ram")
# t=("patil","yadav","patel")
# res=t18+t
# print(res)

# 19. Repeat a tuple containing ("AI", "ML") three times using the * operator.
# t19=("AI","ML")
# print(t19*3)

# 20. Combine two tuples (names and scores) using zip() and convert the result into a tuple.
# names=("ram","shyam","seeta")
# scores=(70,80,90)
# combine=tuple(zip(names,scores))
# print(combine)

# 21. Reverse a tuple using the reversed() function and convert it back to a tuple.
# t21=(1,2,3,4,5,6,7)
# print(tuple(reversed(t21)))

# 22. Find the alphabetically first and last element in a tuple of strings using min() and max().
# t22=("a","b","c","z","f")
# print(min(t22))
# print(max(t22))

# 23. Unpack a tuple of three elements into three separate variables and print them.
# t23=("tom",1,2.5)
# name,i,f=t23
# print(name)
# print(i)
# print(f)

# 24. Create a tuple and demonstrate immutability by trying to modify an element (observe the error).
# t24=(1,2,3,4,5)
# t24[1]=9
# print(t24)

# 25. Compare the memory size of a list and a tuple containing the same elements using sys.getsizeof().

# 26. Create a tuple of 10 numbers and calculate the average using sum() and len().
# t26=(1,2,3,4,5,6,7,8,9,10)
# avg=sum(t26)/len(t26)
# print(avg)

# 27. Create a tuple of city names and print them in reverse order using slicing.
# city=("pune","nagpur","dhule","nashik")
# print(city[::-1])


# 28. Convert a tuple of numbers into a list, append a new number, and convert it back into a tuple.
# t28=(1,2,3,4,5)
# l=list(t28)
# l.append(20)
# print(tuple(l))

