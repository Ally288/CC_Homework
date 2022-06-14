# def fizzbuzz(number):
#     if number == 3:
#         return "Fizz"
#     if number == 5:
#         return "Buzz"
#     return "Fizzbuzz"


def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    else:
        return number
