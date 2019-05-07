# 1. Functions are objects


# def add_five(num):
#print(num + 5)


# add_five(2)

# 2. Functions within functions


# def add_five(num):
# def add_two(num):
# return num + 2

#num_plus_two = add_two(num)
#print(num_plus_two + 3)


# add_five(10)

# 3. Returning functions from functions

# def get_math_function(operation):  # + or -
# def add(n1, n2):
# return n1 + n2

# def sub(n1, n2):
# return n1 - n2

# if operation == '+':
# return add
# elif operation == '-':
# return sub


#add_function = get_math_function('+')
#sub_function = get_math_function('-')
#print(sub_function(4, 6))

# 4. Decorating a function

# def title_decorator(print_name_function):
#   def wrapper():
#      print("Professor:")
#     print_name_function()
# return wrapper


# def print_my_name():
#   print("Matt")


# def print_joes_name():
#   print("Joe")


#decorated_function = title_decorator(print_joes_name)

# decorated_function()

# 5. Decorators

# def title_decorator(print_name_function):
#   def wrapper():
#      print("Professor:")
#     print_name_function()
# return wrapper


# @title_decorator
# def print_my_name():
#   print("Matt")


# @title_decorator
# def print_joes_name():
#   print("Joe")


# print_my_name()
# print_joes_name()

# 6. Decorators w/ Parameters

def title_decorator(print_name_function):
    def wrapper(*args, **kwargs):
        print("Professor:")
        print_name_function(*args, **kwargs)
    return wrapper


@title_decorator
def print_my_name(name, age):
    print(name + " you are " + str(age))


print_my_name("Shelby", 60)
