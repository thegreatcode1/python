# function in python
# function defnition
def hey():
    print("helo")


# function call
hey()

# argument passing inn a function


def hello(name, age):
    print("my name is ", name, 'age:'+str(age))


# hello func call
value = 'suhail'
hello(value, 25)

# tuples
tp = ('hello', "haii", "whatsapp...")
print(tp[0])
"""
this is tuple it is similar to list but tuple are not allowed to modified 
values tuple can only be permit to view the values
"""

# arbitrary argument


def hello1(*values):
    print("first: "+values[0]+" secound: "+values[1],
          values[2])  # values get in to the tuples


hello1("haii", "hello", "how are you")  # like a tuple & func call


# concept of GLOBAL variable & LOCAL variable
val = 10  # this is the globel variable


def sample():
    val = 30  # it is a local variable
    val = val+1  # here  an error 'val+1' val is not resolved in this error will resolve we use 'val = 30'
    s = val+1  # another methord
    # the above three lines are local variables these are not accessed other part of the code
    print(val)  # in this variable can be accesed any way in the whole code
    # here is the 1st example val variable used in to the sample func


print(val)  # here is the 2ed example using outside of the sample func
sample()


# named argument
def sample1(name, age=20):  # default value ,here no argument will pass they will use this default value otherwise use passsed value
    print(name, age)


sample1("suhail", 25)  # normal argument passing
sample1(age=30, name="suhail")  # named argument passing
# use of this type of argument passing is value will pass any ***order****
sample1(name="suhail", age=23)

# sum of two numbers using func


def sum(num1, num2):
    sum = num1+num2  # add two numbers
    return sum  # return the answer to the call of the func


# answer is in the func call, that answer put into the result variable
result = sum(10, 20)
print('result = '+str(result))  # then print it.


# dictionary concept
value1 = {"name": "suhail", "place": "koppam",
          "district": "kollam", "state": "manali", "pin": "688088"}
print(value1)
print(value1.get('place'), value1.get('name'))
# dictionary mainly used backend data get it is a format


# four type of functions
"""
1. Function with no argument and no Return value.
2. With no argument and with a Return value.
3. With argument and No Return value.
4. With argument and Return value.
"""
