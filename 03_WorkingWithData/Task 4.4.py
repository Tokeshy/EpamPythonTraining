### Task 4.4
# Look through file `modules/legb.py`.
# 1) Find a way to call `inner_function` without moving it from inside of `enclosed_function`.
# 2.1) Modify ONE LINE in `inner_function` to make it print variable 'a' from global scope.
# 2.2) Modify ONE LINE in `inner_function` to make it print variable 'a' form enclosing function.
#
# Source :
#
# a = "I am global variable!"
# def enclosing_funcion():
#     a = "I am variable from enclosed function!"
#     def inner_function():
#         a = "I am local variable!"
#         print(a)
#
### 1)

a = "I am global variable!"

def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():
        a = "I am local variable!"
        print(a)
    
    return inner_function()

enclosing_funcion()

### 2)
a = "I am global variable!"
def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():
        global a #a = "I am local variable!"
        print(a)
    
    return inner_function()

enclosing_funcion()

## 3)
a = "I am global variable!"
def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():
        nonlocal a 
        print(a)
    
    return inner_function()

enclosing_funcion()