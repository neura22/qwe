grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
result = {}
i = 0
for student in students:
 result[student] = grades[i]
 i += 1
print(result)
for k in result:
 sum = 0
 v = result[k]
 for i in v:
 sum += i
 result[k] = sum/len(v)

print(result)