### Task 1.1
# Write a Python program to calculate the length of a string without using the `len` function.
SomeEnteredString = input(str())
cn = 0
for ch in SomeEnteredString:
    cn += 1
print(str(cn))