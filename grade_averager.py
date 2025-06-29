grades = []
for i in range(5):
	grades.append(float(input(f"Enter grade #{i+1}: ")))
print(f"Average: {sum(grades)/len(grades)}")
