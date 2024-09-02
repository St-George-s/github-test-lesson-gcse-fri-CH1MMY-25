total_age = 0
for i in range(10):
    age = int(input(f"Enter the age of person {i+1}: "))
    total_age += age
print("The total age is: " + str(total_age))