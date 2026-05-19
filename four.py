#nikhil patil

# 1. Create a dictionary with 5 students and their marks.
# d1={"ram":77,"shyam":88,"tom":99,"seeta":87,"geeta":98}
# print(d1)

# 2. Print the value of a specific student using their name as key.
# d2={"ram":77,"shyam":88,"tom":99,"seeta":87,"geeta":98}
# print(d2["ram"])

# 3. Add a new student with marks to the dictionary.
# d3={"ram":77,"shyam":88,"tom":99,"seeta":87,"geeta":98}
# d3["max"]=86
# print(d3)

# 4. Update the marks of an existing student.
# d4={"ram":77,"shyam":88,"tom":99,"seeta":87,"geeta":98}
# d4["shyam"]=99
# print(d4)

# 5. Delete a student from the dictionary.
# d5={"ram":77,"shyam":88,"tom":99,"seeta":87,"geeta":98}
# del d5["ram"]
# print(d5)

# 6. Print all student names using keys().
# d6={"ram":77,"shyam":88,"tom":99,"seeta":87,"geeta":98}
# for i in d6.keys():
#     print(i)

# 7. Print all student marks using values().
# d7={"ram":77,"shyam":88,"tom":99,"seeta":87,"geeta":98}
# for i in d7.values():
#     print(i)

# 8. Print all student names with their marks using items().
# d8={"ram":77,"shyam":88,"tom":99,"seeta":87,"geeta":98}
# for i,j in d8.items():
#     print(i,j)

# 9. Check if a specific student is in the dictionary.
# d9={"ram":77,"shyam":88,"tom":99,"seeta":87,"geeta":98}
# print("ram" in d9)

# 10. Check if a specific mark is present in the dictionary values.
# d10={"ram":77,"shyam":88,"tom":99,"seeta":87,"geeta":98}
# print(77 in d10.values())

# 11. Use get() to fetch a student's marks safely.
# d11={"ram":77,"shyam":88,"tom":99,"seeta":87,"geeta":98}
# print(d11.get("ram"))


# 12. Create a dictionary of employees with their departments.
# d12={"e1":"HR","e2":"IT","e3":"Sales"}
# print(d12)

# 13. Access the department of a specific employee.
# d13={"e1":"HR","e2":"IT","e3":"Sales"}
# print(d13["e2"])

# 14. Add a new employee and department.
# d14={"e1":"HR","e2":"IT","e3":"Sales"}
# d14["e4"]="marketing"
# print(d14)


# 15. Change the department of an existing employee.
# d15={"e1":"HR","e2":"IT","e3":"Sales"}
# d15["e1"]="civil"
# print(d15)


# 16. Remove an employee from the dictionary.
# d16={"e1":"HR","e2":"IT","e3":"Sales"}
# del d16["e1"]
# print(d16)

# 17. Sort the employee dictionary by employee names in ascending order.
# d17={"b2":"HR","a1":"IT","e3":"Sales"}
# sort=dict(sorted(d17.items()))
# print(sort)

# 18. Sort the employee dictionary by department names in ascending order.
# d18={"b2":"HR","a1":"IT","e3":"Sales"}
# sort=dict(sorted(d18.items(),key=lambda x:x[1]))
# print(sort)

# 19. Sort the employee dictionary by names in descending order.
# d19={"e1":"HR","e2":"IT","e3":"Sales"}
# sort=dict(sorted(d19.items(),reverse=True))
# print(sort)

# 20. Sort the employee dictionary by department in descending order.
# d20={"e1":"HR","e2":"IT","e3":"Sales"}
# sort=dict(sorted(d20.items(),key=lambda x:x[1],reverse=True))
# print(sort)

# 21. Find all keys that have a specific value in a dictionary.
# d21={"e1":"HR","e2":"IT","e3":"Sales"}
# for i,j in d21.items():
#     print(i,":",j)

# 22. Count how many students scored above 80 marks.
# d22={"ram":77,"shyam":88,"tom":99,"seeta":87,"geeta":98}
# count=0
# for i in d22.values():
#     if(i>80):
#         count=count+1
# print(count,"students")

# 23. Create a nested dictionary for 3 students with age, grade, and department.
# d23={
#     1:{"age":21,"grade":"A","department":"IT"},
#     2:{"age":22,"grade":"B","department":"Civil"},
#     3:{"age":23,"grade":"C","department":"Mech"}
# }
# print(d23)


# 24. Access the grade of a student from the nested dictionary.
# d24={
#     1:{"age":21,"grade":"A","department":"IT"},
#     2:{"age":22,"grade":"B","department":"Civil"},
#     3:{"age":23,"grade":"C","department":"Mech"}
# }
# print(d24[1]["grade"])

# 25. Update the department of a student in the nested dictionary.
# d25={
#     1:{"age":21,"grade":"A","department":"IT"},
#     2:{"age":22,"grade":"B","department":"Civil"},
#     3:{"age":23,"grade":"C","department":"Mech"}
# }
# d25[1]["department"]="HR"
# print(d25)

# 26. Loop through the nested dictionary and print student names with their grades.
# d26={
#     1:{"age":21,"grade":"A","department":"IT"},
#     2:{"age":22,"grade":"B","department":"Civil"},
#     3:{"age":23,"grade":"C","department":"Mech"}
# }
# for i,j in d26.items():
#         print(i,j["grade"])

# 27. Merge two dictionaries of students into one.
# students={
# 27:{"ram":1,"shyam":2},
# 28:{"seeta":3,"geeta":4}
# }
# print(students)

# 28. Clear all entries in a dictionary.
# d28= {"ram":1,"shyam":2}
# d28.clear()
# print(d28)

# 29. Copy a dictionary into a new dictionary and modify the copy.
# d29= {"ram":1,"shyam":2}
# copied=d29.copy()
# print(copied)

# 30. Create a dictionary where keys are numbers 1-5 and values are their squares.
# d30={x:x**2 for x in range(1,6)}
# print(d30)









