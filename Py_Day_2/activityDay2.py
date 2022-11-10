# arb_args - Takes in any number of arguments and prints them one at a time.
def arb_args(*args):
    for i in args:
        print(i)

# inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.
def innter_func(a, b):
    def func_1():
        return a+b

    def func_2():
        return a-b
        
    print(func_1()+func_2())

# lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.
def lunch_lady(name, pref="mystery meat"):
    print(name, pref)

# sum_n_product - Accepts two integers and returns both the sum and the product.
def sum_n_product(a,b):
    return a+b, a*b

# alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.
alias_arb_args = arb_args

# arb_mean - Accepts any number of integers and prints their average.
def arb_mean(*args):
    total=0
    for i in args:
        total += i
        print(i/len(args))

# arb_longest_string - Accepts any number of strings and returns the longest one.

def arb_longest_string(*args):
    long = 0
    longest = ""
    for i in args:
        if len(i)>long:
            long=len(i)
            longest = i
    return longest

#if __name__ == "__main__":

lunch_lady("Steve")
lunch_lady("Tammy", "ice cream")