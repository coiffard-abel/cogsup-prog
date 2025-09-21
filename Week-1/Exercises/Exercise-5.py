import math

# Helper function: Ignore
def sprint(s):
    if __name__ == "__main__":
        print(s)

################################################################################
"""
Recommended readings: 
  Chapter on functions: https://automatetheboringstuff.com/3e/chapter4.html
"""
################################################################################

"""
Exercise 5.1

Task:
------
Go back to the code you wrote for exercise 2.7 and turn it into a function called print_triangle_o.
The function should take one argument called 'rows' and print a triangle out of 'o's with n rows.
"""

sprint("Exercise 5.1")

def print_triangle_o(rows):
    for i in range(rows):
        for j in range(rows-i-1):
            print(" ", end='')

        for j in range(2*i+1):
            print("o", end='')
        print('')
    pass

print_triangle_o(3)

sprint("---")

"""
Exercise 5.2

Task:
------
Go back to the code you wrote for exercise 3.2 and turn it into a function called prod_list_easy.
You can assume that all the elements of the list are numbers.
"""

sprint("Exercise 5.2")

def prod_list_easy(lst):
    return math.prod(lst)

print(prod_list_easy([1, 2, 3, 4, 5, 6]))

sprint("---")

"""
Exercise 5.3

Task:
------
Go back to the code you wrote for exercise 3.2 and turn it into a function called prod_list_rec.
You can assume that all the elements of the list are numbers but you are not allowed to use
loops.

Hint: Can you think of a recursive way to do it?
------
"""

sprint("Exercise 5.3")

def prod_list_rec(lst):
    sum = 0
    for num in lst:
        sum = sum + num*num
    return sum

print(prod_list_rec([1, 2, 3, 4]))

sprint("---")

"""
Exercise 5.4

Task:
------
Take the function body you wrote in the previous exercise and modify it so that it stops
executing in case not all of the elements of the list are numbers.

Hint: The product of the empty set is 1.
------
"""

sprint("Exercise 5.4")

def prod_list_rec_full(lst):
    sum = 0
    for num in lst:
        if not(type(num) == int or type(num) == float):
            print("Type Error")
            sum = None
            break
        else:
            sum = sum + num*num
    return sum

print(prod_list_rec_full([1, 3, 5, 7, 9, "abricot"]))

sprint("---")

"""
Exercise 5.5

Task:
------
Once you have solved Exercises 5.1 to 5.4, uncomment the following lines of code
and run the script again. The lines of code test the functions you wrote against
expected outputs. If you solved the exercises correctly, the script will tell you.
------
"""

## Run test cases
if __name__ == "__main__":
     from testcases import (
         run_tests_ex51,
         run_tests_ex52,
         run_tests_ex53,
         run_tests_ex54,
     )

     run_tests_ex51()
     run_tests_ex52()
     run_tests_ex53()
     run_tests_ex54()