# Imports

# Global Variables

# Main
print('')  # Line feed
number = input('Please enter a number:  ')
number2 = input('Please enter a second number:  ')

# Convert to integers:
number = int(number)
number2 = int(number2)

print('')  # Line feed
# Odd numbers aren't divisible by 2
if number % 2:
    print('Your number is an odd number')
else:
    # If number is a multiple of 4 (# % 4 = 0)
    if not number % 4:
        print('Your number is a multiple of 4')
    else:
        print('Your number is an even number')

# If number divisible by number2 (no remainder)
if not number % number2:
    print('Your number is evenly divisible by your second number')
else:
    print('Your number is not evenly divisible by your second number')
print('')  # Line feed

