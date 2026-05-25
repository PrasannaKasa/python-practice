from functools import reduce
add = lambda*nums:sum(nums)
multiply = lambda*nums:reduce(lambda x,y :x*y,nums)
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n*factorial(n-1)
operations = {"add":add,"multiply":multiply,"factotial":factorial}
def function(*args):
    return operation[operations][nums]
print(add(5,6))
print(multiply(4,5))
print(factorial(5))