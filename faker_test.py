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

def name_len(x):
    return len(x)

l = [x.split()[0] for x in [fake['ro_RO'].name() for _ in range(10)]]
# l.sort(key= lambda _: len(_))

print(l)

p = [fake['ro_RO'].phone_number() for _ in range(10)]
print(p)

e = [fake['ro_RO'].email() for _ in range(10)]
print(e)

b = [fake['ro_RO'].license_plate() for _ in range(10)]
print(b)