names = ['Charlie', 'Kesh', 'Annah', 'Emily', 'Lailah']
upper_case = map(str.upper, names)
print(list(upper_case))

numbers  =[1, 2,3,4,5]
squares  = map(lambda x: x**2, numbers)
print(list(squares))

names  = ['Alysa', 'Alice', 'Bob', 'Elizabeth', 'Benjamin']
ages = [9, 5, 7, 10, 8]
grades  = ['A', 'C', 'F','D', 'B'] 

combined  =zip(names, ages, grades)
print(list(combined))


numbers = [1,2,3,4,5,6]
even = [x for x in numbers if x%2==0]
print("Th even numbers are", even)


for i in range(10):
    if i == 5:
        print(exit)
        exit()
    print(i)
    break
