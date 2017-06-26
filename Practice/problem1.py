# Imports
import time

# Global Variables

# Main
print('\nWelcome!')
name = input("What's your name? ")
age = input('How old are you? ')
count = input('How many times would you like to see the result? ')

futage = 100 - int(age)
futyear = int(time.strftime('%Y')) + futage

print('')  # Line feed
for i in range(int(count)):
    print("Well " + name + ", you'll turn 100 in " + str(futyear) + ".")
print('')  # Line feed

