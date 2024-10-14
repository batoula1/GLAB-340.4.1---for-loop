n = int(input("Enter a positive integer (n): "))

sum_of_natural_numbers = 0


# Calculate the sum of the first 'n' natural numbers
for i in range(1, n + 1):
    sum_of_natural_numbers += i


# Display the sum
print(f"The sum of the first {n} natural numbers is: {sum_of_natural_numbers}"