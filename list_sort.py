marks = ['Comp = 99', 'Phy = 74', 'Maths = 88', 'Eng = 56']
print("Marks before sorting: ")
print(marks)

marks.sort(key=lambda n: n[1])
print("\nMarks after sorting: ")
print(marks)
