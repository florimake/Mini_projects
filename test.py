from math import sqrt

# def find_next_square(sq):
#     if (sqrt(sq) % 2 == 1) and (sq > 0):
#         return int((sqrt(sq)+1))**2
#     elif (sqrt(sq) % 2 == 0) and (sq > 0):
#         return int(sqrt(sq)+1)**2
#     elif sq == 0:
#         return 1
#     else:
#         # return the next square if sq is a square, -1 otherwise
#         return -1
    
def find_next_square(sq):
    return ((sq ** 0.5) + 1) ** 2 if sq%(sq ** 0.5) == 0 else -1
    
# print(find_next_square(14))

# 123456.0

# print(14 ** 2)
# print(12*16)


def printer_error(s):
    color = 'abcdefghijklm'
    accepted = [x for x in s if x.lower() in color]
    not_accepted = [x for x in s if x.lower() not in color]
    return f"{len(accepted)}/{len(not_accepted)}"
    
    
    
    
    
# print(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))

"""
Example:

Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
"""
def to_jaden_case(string):
    print(" ".join([x.capitalize() for x in string.split()]))
    
    
# to_jaden_case("How can mirrors be real if our eyes aren't real")


"""
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
"""
from random import randint
def descending_order(num):
    n = [x for x in str(num)]
    n.sort()
    n = n[::-1]
    print(int("".join(n)))
        
    


# descending_order(123456789)



    """
You are given an array (which will have a length of at least 3, but could be very large) 
containing integers. The array is either entirely comprised of odd integers or entirely comprised 
of even integers except for a single integer N. Write a method that takes the array as an argument 
and returns this "outlier" N.
    Examples:
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
    """
    
def find_outlier(integers):
    return int([x for x in integers if x % 2 == 0][0]) if len([x for x in integers if x % 2 == 0])==1 else int([x for x in integers if x % 2 == 1][0])

# print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
# print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
# # Expected: 160
# print(find_outlier( [-6417808, 35304, -248952, 5111769, -9539456, 2376594, 1511512, -2448360, -1170178, 4174958, 5202832, 2869508, 429816, -9486238, 2663276, 2689212, -4244116, 2382142, -2999974, -8920658, -105636, -5490228, -5149730, -1593418, 660020, 9008616, -5616540, 6416952, -7517608, 9372976, -6274718]))
# # Expected: 5111769
# print(find_outlier( [36062, 6150610, 4339114, 5650268, 1568756, 2076054, -6280362, -2201970, 9176998, 9978534, -9151770, -596230, -4460381, -2123530, 8866808, 9683910, -5616000, 6497448, -4855490]))
# # Expected: -4460381


    """
    Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

If you want to know more: http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

Example: (input --> output)

"ATTGC" --> "TAACG"
"GTAT" --> "CATA"
    """
    
def DNA_strand(dna):
    d = []
    print(dna)
    for x in dna:
        if x == "T":
            d.append("A")
        elif x == "A":
            d.append("T")
        elif x == "G":
            d.append("C")
        elif x == "C":
            d.append("G")
        elif x not in "TAGC":
            d.append(x)
    return "".join(d) 
    
    
print(DNA_strand("ATTGC"))

import os

print(os.getcwd())

from collections import OrderedDict
from faker import Faker
Faker.seed(0)
locales = OrderedDict([
    ('en-US', 1),
    ('en-PH', 2),
    ('ja_JP', 3),
    ('ro_RO', 6),
])
fake = Faker(locales)

# b = [fake['ro_RO'].profile()['birthdate'] for _ in range(10)]
# for x in b:
#     print(str(x.strftime("%d-%m-%Y")))
    
# a = [fake['ro_RO'].date_between("-30y", "-15y") for _ in range(10)]
# for x in a:
#     print(str(x.strftime("%d-%m-%Y")))
