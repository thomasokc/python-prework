# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    """Prints a username"""
    print("hello_" + user_name + "!")

user_name = input("What is your username? ")

hello_name(user_name)



# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    """Prints odd numbers from 1-100"""
    for i in range(1,101):
        if i % 2 == 1:
            print(i)

print(first_odds())



# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

numbers_list = [3,7,1,4,5,9,2,8,6]
animal_list = ['wolf', 'snail', 'koala', 'python', 'eagle']

def max_num_in_list(a_list):
    """Returns max number of a list"""
    sorted_list = max(a_list)
    return str(sorted_list)

answer1 = max_num_in_list(animal_list)
answer2 = max_num_in_list(numbers_list)

print("The max num is "+ answer1)
print("The max num is "+ answer2)



# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    """Checks to see if the year is a leap year"""
    if a_year % 4 == 0 and a_year % 100 == 0 and a_year % 400 == 0:
        return True
    elif a_year % 4 == 0 and a_year % 100 != 0:
        return True
    else:
        return False

year_check = input("Enter a year to check if it is a leap year! ")
year_check = int(year_check)
print(is_leap_year(year_check))



# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

good_numbers = [1,2,3,4,5,6,7,8,9]
opposite_numbers = [9,8,7,6,5,4,3,2,1]
random_numbers = [42,1,89,5]
more_numbers = [10,11,12,13,14,15]

def is_consecutive(a_list):
    """Checks to see if numbers are consecutive"""
    list_copy = a_list[:]
    for copy in list_copy:
        consecutive = copy + 1
        break
    for number in a_list:
        if number + 1 == consecutive:
            number += 1
            consecutive += 1
        else:
            return False
    return True

print(is_consecutive(good_numbers))
print(is_consecutive(opposite_numbers))
print(is_consecutive(random_numbers))
print(is_consecutive(more_numbers))