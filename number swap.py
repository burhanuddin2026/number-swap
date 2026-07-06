num1 = 5
num2 = 10

print("Before swap:")
print("num1 =", num1)
print("num2 =", num2)

# Step 1: Store num1's value in temp
temp = num1

# Step 2: Put num2's value into num1
num1 = num2

# Step 3: Put the saved value (from temp) into num2
num2 = temp

print("\nAfter swap:")
print("num1 =", num1)
print("num2 =", num2)