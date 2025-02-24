# 🎉 Welcome to the Fun Calculator! 🎉
# We're going to add, subtract, multiply, and divide two numbers like a boss! 😎

# Step 1: Ask the user to input the first number
num1 = float(input("Enter the first number: "))

# Step 2: Ask the user to input the second number
num2 = float(input("Enter the second number: "))

# Step 3: Time to do some math! 🧠
# Compute the sum, difference, product, and quotient.

sum_result = num1 + num2  # ➕
difference_result = num1 - num2  # ➖
product_result = num1 * num2  # ✖️

# Handle division carefully to avoid division by zero
if num2 != 0:
    quotient_result = num1 / num2  # ➗
else:
    quotient_result = "Undefined (cannot divide by zero)"  # 🚫

# Step 4: Display results 🎉
print("\nResults of your two numbers:")
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Quotient: {quotient_result}")

# 🏁 And that's it! You've just made a mini-calculator! 😎💻
