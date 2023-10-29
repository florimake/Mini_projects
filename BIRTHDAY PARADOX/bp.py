import random

insert = int(input("introdu ub numar de date de nastere: "))
start_repeat = 10000
repeat = start_repeat
mach = 0


while repeat != 0:
    d = [f"{random.randint(1,31)}-{random.randint(1,12)}" for _ in range(insert)]
    drw = set(d)
    repeat -= 1
    # mach += int(len(d)-len(drw))
    if len(drw) < len(d):
        mach += 1
    
        
print(f"From {insert} - {mach} is repeat")
print(f"Out of {start_repeat} simulations of {insert} people, there was a\nmatching birthday in that group {mach} times. This means\nthat {insert} people have a {mach/start_repeat*100} % chance of\nhaving a matching birthday in their group.\nThat's probably more than you would think!")


    