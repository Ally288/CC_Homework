# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:


# 2. Print the difference between the largest and smallest value:

print(max(numbers) - min(numbers))

# 3. Print True if the list contains a 2 next to a 2 somewhere.

pointer = 0
for number in numbers:
    if number == pointer and number == 2:
        print("True")
    pointer = number

for index, number in enumerate(numbers):
    if number and numbers[index - 1]:
        print("True")

# 4. Print the sum of the numbers,
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

total = 0  # starts at zero
check = False
for n in numbers:
    if n == 6:
        check = True
    if check == False:
        total += n
    if n == 7:
        check = False

print(total)

# 5. HARD! Print the sum of the numbers.
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5.

total = 0

for index, number in enumerate(numbers):
    if number != 13 and number[index + 1] != 13:
        number = total
