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
    
print(find_next_square(14))

123456.0

print(14 ** 2)
print(12*16)


def printer_error(s):
    color = 'abcdefghijklm'
    accepted = [x for x in s if x.lower() in color]
    not_accepted = [x for x in s if x.lower() not in color]
    return f"{len(accepted)}/{len(not_accepted)}"
    
    
    
    
    
print(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))