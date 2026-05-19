#nikhil patil

# 1. Create a set containing five different country names and print it.
# s1={"india","usa","france","canada","germany"}
# print(s1)

# 2. Create a set with duplicate numbers and print it to see how duplicates are handled.
# s2={1,2,2,3,4,5,3,4}
# print(s2)

# 3. Use the set() constructor to create a set from a list of fruits.
# l3=["apple","banana","mango","orange"]
# s3=set(l3)
# print(s3)

# 4. Add a new element into an existing set using add() method.
# s4=set()
# s4.add(5)
# print(s4)

# 5. Add multiple elements into a set using update() method.
# s5=set()
# s5.update([1,"mango",2,"orange"])
# print(s5)

# 6. Try adding a duplicate element to the set and check if it changes.
# s6={1,2,3,4,5}
# s6.add(5)
# print(s6)

# 7. Remove an element from a set using remove() method.
# s7={1,2,3,4,5}
# s7.remove(5)
# print(s7)

# 8. Remove an element safely using discard() without raising an error.
# s8={1,2,3,4,5}
# s8.discard(5)
# print(s8)

# 9. Remove a random element using pop() and print both removed and remaining elements.
# s9={1,2,3,4,5}
# res=s9.pop()
# print(s9)
# print(res)

# 10. Clear all elements from a set using clear() and print it.
# s10={1,2,3,4,5}
# s10.clear()
# print(s10)

# 11. Create two sets of numbers and perform union operation.
# s11={1,2,3}
# s12={3,4,5}
# res=s11 | s12
# print(res)

# 12. Perform intersection between two sets to find common elements.
# s12={1,2,3,4}
# s13={3,4,5,6}
# res=s12 & s13
# print(res)

# 13. Perform difference between two sets to find unique elements from the first set.
# s13={1,2,3,4}
# s14={3,4,5,6}
# res= s13 - s14
# print(res)

# 14. Perform symmetric difference between two sets and print the result.
# s14={1,2,3,4}
# s15={3,4,5,6}
# res= s14 ^ s15
# print(res)

# 15. Check if one set is a subset of another using issubset() method.
# s15={1,2,3}
# s16={1,2,3,4,5,6}
# print(s15.issubset(s16))

# 16. Check if one set is a superset of another using issuperset() method.
# s16={1,2,3,4,5,6}
# s17={1,2,3}
# print(s16.issuperset(s17))

# 17. Check if two sets have no common elements using isdisjoint() method.
# s17={1,2,3}
# s18={4,5,6}
# print(s17.isdisjoint(s18))

# 18. Use in keyword to check if a particular element exists in a set.
# s18={"apple",1,2,3}
# print("apple" in s18)

# 19. Use not in keyword to check if an element does not exist in a set.
# s19={"apple",1,2,3}
# print("banana" not in s19)

# 20. Find the total number of elements in a set using len().
# s20={1,2,3,4,5}
# print(len(s20))

# 21. Find the maximum and minimum element from a numeric set using max() and min().
# s21={21,1,2,3,50,5,6}
# print(max(s21))
# print(min(s21))

# 22. Find the sum of all elements from a numeric set using sum().
# s22={1,2,3,4,5}
# print(sum(s22))

# 23. Convert a set into a sorted list in ascending order using sorted().
# s23={4,5,6,2,3,1}
# res=sorted(s23)
# print(res)

# 24. Sort a set in descending order using sorted() with reverse=True.
# s24={1,2,3,4,5,6}
# res=sorted(s24,reverse=True)
# print(res)

# 25. Use any() to check if at least one True value exists in a Boolean set.
# s25={1,1,1}
# print(any(s25))

# 26. Use all() to check if all values in a Boolean set are True.
# s26={1,1,1}
# print(all(s26))

# 27. Copy a set using copy() and verify both sets are independent.
# s27={1,2,3,4,5}
# copied=s27.copy()
# print(copied)
# print(s27)

# 28. Delete a set completely using del keyword and observe the result.
# s28={1,2,3,4,5}
# del s28
# print(s28)

# 29. Convert a list with duplicate values into a set to remove duplicates.
# li=[1,1,2,2,3,3,4,4,5,5]
# res=set(li)
# print(res)

# 30. Create two sets of student names (from two different classes) and find:
#     a) Common students (intersection)
#     b) Students only in class A (difference)
#     c) All unique students (union)
# s30={"raj","rahul","ram"}
# s31={"ram","shyam","seeta"}
# res= s30 & s31
# print(res)
# res1= s30 - s31 
# print(res1)
# res2= s30 | s31
# print(res2)

