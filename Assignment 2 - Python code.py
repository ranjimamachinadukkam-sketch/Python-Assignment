age_list = [24, 25, 26, 27, 28]
name_list = ["Anu", "Rahul", "Meena", "Arun", "Vijay"]

print("Age List:", age_list)
print("Name List:", name_list)



# a. Append
name_list.append("Yazhini")
print("After append:", name_list)

# b. Insert 30 at index 2
age_list.insert(2, 30)
print("After inserting 30:", age_list)

# c. Remove Yazhini
name_list.remove("Yazhini")
print("After removing Yazhini:", name_list)

# d. Pop last element
age_list.pop()
print("After popping last element:", age_list)

# e. Extend age_list
age_list.extend([29, 30, 26])
print("After extending:", age_list)

# f. Sort in descending order
age_list.sort(reverse=True)
print("Descending order:", age_list)

# g. Maximum, minimum and sum
print("Maximum age:", max(age_list))
print("Minimum age:", min(age_list))
print("Sum of ages:", sum(age_list))



print("First element:", name_list[0])
print("Last element:", name_list[-1])
print("Index 2 to 4:", name_list[2:5])
print("Reverse order:", name_list[::-1])


# Dictionary

student_marks = {
    "Anu": 75,
    "Rahul": 88,
    "Meena": 92,
    "Arun": 68,
    "Vijay": 85
}

# b. Access a student's mark
print("Meena's mark:", student_marks["Meena"])

# c. Add Janani
student_marks["Janani"] = 80
print("After adding Janani:", student_marks)

# d. Update Arun's mark
student_marks["Arun"] = 82
print("After updating Arun:", student_marks)

# e. Keys, values and items
print("Keys:", student_marks.keys())
print("Values:", student_marks.values())
print("Key-value pairs:", student_marks.items())

my_set = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}

print("My set:", my_set)

# Sets do not support indexing
# my_set[4] = 's'   # This gives TypeError

my_set.add('s')
print("After adding s:", my_set)


set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}

print("Set 1:", set1)
print("Set 2:", set2)

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))

score = float(input("Enter your score (0-10): "))

if score < 0 or score > 10:
    print("Invalid score. Please enter a score between 0 and 10.")

elif score > 7:
    print("Above Average")
    print("Great performance! Keep it up.")

elif score >= 4:
    print("Average")
    print("Good performance! Keep practicing.")

else:
    print("Below Average")
    print("Need to improve your performance. Consistent practice will lead to better results.")
