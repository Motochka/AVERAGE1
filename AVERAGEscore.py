grades= [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve','Kendril', 'Aaron'}
aver=[sum(column)/len(column) for column in grades]
#print(aver)
sorted_list=sorted(students)
#print(sorted_list)
result=dict(zip(sorted_list,aver))
print(result)