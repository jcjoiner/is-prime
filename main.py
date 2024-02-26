# Problem Set 8
# Is Prime or Not?

'''
    Implement a function that checks if a given number is prime or not.
'''

# Ask user for a number
# Check if number <= 1
# Iterate over a range to check if number is prime
# Print results to user

def is_prime():
    num = int(input("Enter a number: "))

    if num <= 1:
        print("Numbers must be greater than 1.")

    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number.")
        else:
            print(f"{num} is a prime number.")
        break

is_prime()
