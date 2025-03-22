import math
import random  # everything will be imported
from math import ceil, floor, exp, log, log10, modf, sqrt  # importing individually


def sort_second(val):  # function
    return val[1]


# this is comment
print('single inverted comma')
print("double inverted comma")
print('''triple single inverted comma''')
print("""triple double inverted comma""")
print('i\'m planning to write a "book"')  # to use single and double inverted commas inside inverted comma

# identifiers naming types
ide = 10
_ide = 11
_10 = 12; Ide_2 = 13  # multiple statements on single line
ide_1 = "python \
        program"  # multi line statement

# variables
a = 8  # int
b = 1.2  # float
c = 'a'  # string
d = True  # boolean   or
e, f = 1, 1.2  # we can also assign value in this way
g = h = 1  # e and f will have same values
print('multiple variable print', a, b, c, d)  # will print values with space
print('type of each variable', type(a), type(b), type(c), type(d))  # will print type of those variables
print('65 is ASCII of', chr(65))
print('ASCII of A is', ord('A'))

# data types
# number
k = -10  # int
m = 12.2  # float
n = 2 + 1j  # complex
# int
print('int conversion', int(m))  # converts other type to int
print('absolute value', abs(k))  # distance between negative value to zero
print('exponential value', exp(a))  # exponential
print('maximum value', max(k, a))  # gives maximum value
print('minimum value', min(k, a))  # gives minimum value
# float
print('float conversion', float(k))  # converts other type to float
print('round off to max', ceil(m))  # float number to integer 1.1 will be 2
print('round off to min', floor(m))  # float number to integer 1.1 will be 1
print('2 values after and before decimal point', modf(m))  # gives 2 values fraction value and integer value
# complex
print('converts to complex', complex(k))  # converts other type to complex, here imaginary part is zero, for two
# numbers as follows
print(complex(k, m))
print('real part', n.real)  # will print real part
print('imaginary part', n.imag)  # will print imaginary part
print('- to +, + to -', n.conjugate())  # 2-1j will be printed
print('log of 100 is', log(100))  # log value
print('log 10 of 10 is', log10(10))  # log to base 10
print('2^4 is', (pow(2, 4)))  # gives 2 to the power of 4
print("round off", round(1.225))  # round off
print("round off till second decimal value", round(1.225, 2))  # round off .225 to .23 will round off second value
print('sqrt of 100', sqrt(100))  # square root
print("cube root", math.cbrt(a))  # cube root
print("greatest common divisor", math.gcd(ide, _ide))  # gcd
print(" least common multiple", math.lcm(ide, _ide))  # lcm
del a, b, c, d, e, f, g, h, k, m, n  # will delete variables

# string
var_1 = "mynameisvijay"
var_2 = "what", "is", "your", "name?"
var_3 = "my\tname is Vijay"
var_4 = "my\nname is Vijay"
print('string', var_1)
print('length of string is', len(var_1))  # gives length of string
print(var_1.count('m'))  # number of times m got repeated
print(var_1.index('is'))  # it will give index number of 'is' from string
print(var_1.rindex('a'))  # it will give index number from right
print(var_1.rindex('a', 0, len(var_1)))
print('maximum character', max(var_1))  # it will give maximum character available in given string
# (according to ascii number) here y is biggest
print('minimum character', min(var_1))  # it will give minimum character available in given string
print(var_1[0])  # read each or multiple character, white space neglected
print(var_1[0:4])  # 0:4 means 0,1,2,3
print(var_1[5:])
print(var_1 + var_1)  # concatenation
print(var_1 * 2)  # repetition
print(var_1.find("a"))  # to search char or str
print(var_1.rfind('i', 0, len(var_1)))  # it will give the highest index
print(var_1.rfind('n', 4))  # searches from fourth index it will return -1 if not found
print("vijay" in var_1)  # it will find if vijay is available in given string or not
print(var_1.replace("vijay", "krishna", 1))  # replaces vijay by krishna,(if vijay repeated twice it will replace once)
# but it will create new string keeps old as it is
in_tab = 'aeiou'
out_tab = '12345'
transtab = var_1.maketrans(in_tab, out_tab)  # it will replace values of var_1 containing in_tab values by out_tab
print(transtab)  # it will print some ascii values(translate table)
print(var_1.translate(transtab))  # ascii to readable format(translate table)
print("hello {}, your balance is {}".format("vijay", 25))  # formats given string into nicer output
print("hello {0}, your balance is {1}".format("vijay", 25))  # by using position(can also mix with next one)
print("hello {name}, your balance is {money}".format(name="vijay", money=25))  # by using keys and values
ext = {'name': 'vijay', 'money': 25}
print("hello {name} your balance is {money} ".format(**ext))  # creates new dictionary
print("hello {name} your balance is {money} ".format_map(ext))  # similar to format(**ext) doesn't create dictionary
print(var_1.upper())  # upper case
print(var_1.lower())  # lower case
print(var_1.title())  # converts each first letter to capital letter
print(var_1.capitalize())  # to convert first letter to capital letter
print(var_1.casefold())  # converts every char in a given string to lower case
print(var_3.swapcase())  # swaps from lower to upper and vice versa
print(" ".join(var_2))  # joins multiple objects of one string
print(var_3.expandtabs(16))  # this will give a tab at \t default is 8
enc = var_1.encode('utf-8', errors='strict')  # errors are error handling scheme, utf-8 is type of encoding
print(enc)
print(enc.decode('utf-8', 'strict'))
print(var_1.center(30, ' '))  # in 30 spaces var_1 will print at center
print(var_1.zfill(25))  # copy of string with zero padded on left(25 is width or new length)
print(var_1.ljust(25, '*'))  # if length is greater than or equal to 25 then it will print as it is else it will print
# *, default is white space
print(var_1.rjust(25, '*'))  # similar to l just but it will print * in beginning
print(var_3.split())  # splits sentence into individual values(creates list)
print(var_3.split('y', 1))  # splits at y and only once(creates list)
print(var_3.rsplit('y', 1))  # splits at y and only once from right(creates list)
print(var_4.splitlines())  # splits at line breaking character(creates list)
print(var_1.strip('my'))  # removes white spaces in leading and tailing end(y is at the end, so it will remove it)
print(var_1.lstrip('m'))  # trim or remove char given in left strip
print(var_1.rstrip('y'))  # trim or remove char given in right strip
print(var_1.partition('name'))  # splits at 'name' and returns as tuples
print(var_1.rpartition('a'))  # splits at 'a' from right and returns as tuples(only once)
suf = 'vijay'
print(var_1.startswith(suf))  # if value of suf begins in the given string then it will produce true
print(var_1.endswith(suf))  # if value of suf ends in the given string then it will produce true
print(var_1.endswith(suf, 0, 10))  # within 0-9 places of string (false)
print(var_1.isalnum())  # to find any alphanumerical(alphabet and numbers no space) value available in string
print(var_1.isalpha())  # to find out given string is of only alphabetic(no space)
print(var_1.islower())  # to find out given string has only lowercase or not
print(var_1.isdigit())  # to find out given string has only digit or not
print(var_1.isspace())  # to find out given string has white space or not
print(var_1.istitle())  # to find out first letter of each word in given string is uppercase or not
print(var_1.isupper())  # to find out given string is in capital letter or not
print(var_1.isnumeric())  # similar to isdigit but for unicode
print(var_1.isprintable())  # gives true when it has printable characters if \n present then it will generate false
print(var_1.isascii())  # if given string is inside defined ascii values then it is true
print(var_1.isidentifier())  # if valid identifier then true(vijay10,vijay) else false(10vijay, vi jay)
print(var_1.isdecimal())  # similar to isnumeric and isdigit

# list
# similar to array in C but list contains different types
lis1 = [1, 6, 8, 5, 9]  # list with numbers
lis2 = ['ant', 'a', 5.2, 3]  # list with multiple type object
lis3 = [1, [2, 5, 4]]  # nested list
lis5 = [(1, 4), (3, 2), (5, 1)]
print('first list with only int', lis1)
print('second list with all types', lis2)
print('nested list', lis3)
print('reading individually', lis1[0])  # reading individual element
print('reading individually in reverse', lis1[-1])  # reading individual element in reverse
print('reading from beginning to some extent', lis1[0:3])  # only 3 elements will be printed (slicing list)
print('reading from somewhere to end', lis1[3:])  # prints from 4th element (slicing list)
print('reading individual character from list', lis2[0][2])  # reading individually (slicing list)
print('reading from nested list', lis3[1][1])  # (slicing list)
print('concatenating lists', lis1+lis2)  # (slicing list)
print('repeating any list', lis1*2)  # (slicing list)
lis4 = lis1.copy()  # else original list will be altered during changing list values
lis4[0] = 2  # changing list values individually
print('original list', lis1, 'modified list', lis4)
lis4[1:4] = [6, 5, 4]
print('modify multiple values', lis4)
lis4.reverse()
print('reversed list', lis4)
reverse = lis4[::-1]
print('reverse list using slice', reverse)
for a in reversed(lis4):
    print(a)
lis4.sort()
print('sorted list', lis4)
lis1.sort(reverse=True)
print('sorting in descending order', lis1)
sot = sorted(lis4, reverse=True)
print('sorting in descending order(2nd method)', sot)
lis5.sort(key=sort_second)  # sorting using key values
print(lis5)
lis1.append(6)  # if [6,4] is used like extend then it will create nested list
print('append(add individually to list', lis1)
lis1.extend([4, 5])
print('add multiple to the list', lis1)
lis1.insert(0, 10)  # will insert on 0th position in list
print('inserting in desired location', lis1)
lis1[0:0] = [12, 13]  # for multiple insert
print('inserting multiple values in desired location', lis1)
lis1.remove(8)  # removes given value
print('removes given value', lis1)
lis1.pop()
print('pop() removes last value', lis1)
lis1.pop(1)
print('pop(1) removes value from given location', lis1)
lis1[0:2] = []
print('one kind of clearing list', lis1)
lis1.clear()
print('clear list', lis1)
print('index value of given list element is', lis4.index(4))  # for repeated values index of first is returned
print('searching index value of given element in given range', lis4.index(4, 1, 5))  # searching 4
print('searching index value of given element from given index', lis4.index(4, 1))
del lis4[0]
print('deleting individually', lis4)
del lis1[6:10]
print('deleting multiple values', lis1)
del lis4  # will show error
# print('list got deleted', lis4)

# random list
random.seed()  # initialize basic random number generator
print(random.random())  # gives random value from 0.0-0.999...
list_2 = [2, 3, 4, 5]
random.shuffle(list_2)  # shuffle list
print(list_2)
print(random.choice(list_2))  # gives random number from list
print(random.randrange(100))  # gives one random number from 0-99
print(random.randrange(0, 100, 2))  # gives any numbers which gives remainder as zero when divided by 2 from 0-98
print(random.uniform(5, 10))  # gives value between 5-10 with floating value

# tuple
# use tuple("any list, set") for conversion
tuple_1 = (1, 2.3, "vijay")
print("tuple", tuple_1)
tuple_2 = (3, 2, 9, 8)
print("accessing individual values", tuple_1[1])
print("concatenate", tuple_1+tuple_2)
print("length of tuple", len(tuple_2))
print("max value in tuple", max(tuple_2))
print("min value in tuple", min(tuple_2))

# dictionary
di_1 = {1: 2, 3: 4, 5: 6}  # keys:values
di_2 = {1: 2, 3: 4, 1: 0}
print("dictionary", di_1)
print("reading dictionary values using keys", di_1[1])  # using keys only
# di_2[1] will read second value '0' repeated keys not allowed
di_1[1] = 0
print("changing values for given key value", di_1)
di_1[7] = 8
print("adding values", di_1)
print(len(di_1))  # gives length (keys only)
print(str(di_1))  # just provides new string representation
del di_1[1]  # will delete '1' key and its value
# del di_1  will delete everything even var name
# di_1.clear() will clear everything inside var
# dict.clear(di_1)  will clear everything
di_3 = dict.copy(di_1)  # will copy from one dictionary to another
seq_keys = {1, 2, 3}
di_4 = dict.fromkeys(seq_keys, 10)  # creates dictionary with keys from seq_keys and its values as 10
print("will create dictionary with keys from seq_keys and its values as 10", di_4)
print(di_1.get(1))  # will get values of di_1 for 1 key
# di_1.setdefault(1) similar to get()
print(di_1.items())  # will get list containing tuples of keys and values each
print(di_1.keys())  # will get keys of that dictionary
di_1.update(di_4)  # will update or add di_4 to di_1
print("after update", di_1)
print(di_1.values())  # will print values in given dictionary

# Arithmatic
a = 10
b = 7
s1 = a+b
s2 = a-b
s3 = a*b
s4 = a/b
s5 = a % b
s6 = a//b
s7 = a**b
print('add', s1, 'sub', s2, 'multiply', s3, 'divide', s4, 'remainder', s5, 'quotient', s6, 'modulus or power', s7)
print('equal or not', a == b, a != b)
print('less than or greater than or equal', a > b, a < b, a >= b, a <= b)
print(bin(a), bin(b))  # will give binary format of given number
print('bitwise and', bin(a & b), 'or', bin(a | b), 'xor', bin(a ^ b), 'ones compliments', bin(~ a))
print('bitwise left shift', bin(a << 2), 'right shift', bin(a >> 2))
if a == 10 and b == 7:
    print('and logical operation')  # similar way we can use or
c = True
print('not logical', not c)

# membership operator
q = 3
if q in range(5):
    print('yes')
if q not in range(2):
    print('yes')

# identity operator
r = 3
if q is r:
    print('yes')
if q is not r:
    print('no')

# if statement
if r in range(2, 6):
    print('if condition passed')
if r in range(4, 6):  # if else
    print('if condition passed')
else:
    print('if condition failed')
if r in range(4, 6):  # elif
    print('if condition passed')
elif r in range(2, 6):
    print('elif condition passed')
else:
    print('if and elif condition failed')
if r in range(2, 6):  # nested if
    print('first if')
    if r in range(2, 5):
        print('nested if')
else: print('nested failed')  # single statement suite

# loops
# loops supports nested
while r < 6:
    print('while loop call')
    r += 1  # no increment it will go infinite loop
print('while loop ends')
# we can also use else instead of direct print above
# also supports single line suite

for w in range(2, 7):
    print(w, 'w will have values beginning from 2-7 in for loop')

# loop control
for w in range(0, 100):
    if w == 40:
        break  # can also be used for while loop
print('break will break out of for loop')
for w in range(0, 100):
    if w == 40:
        continue  # can also be used for while loop
print('continue will never execute codes which are next to it')
while r < 30:
    r += 1
    if r == 20:
        pass  # if there are no statements to be written for now just use pass to fix error

