import sys

if len(sys.argv) != 4:
    print("Usage: python script.py <first> <last> <domain>")
    sys.exit(1)

first = sys.argv[1]
last = sys.argv[2]
domain = sys.argv[3]

patterns = [
    "{first}{last}",
    "{first}.{last}",
    "{f}{last}",
    "{first}{l}",
    "{f}.{last}",
    "{first}_{last}",
    "{last}{first}",
    "{last}.{first}",
]

f = first[0]
l = last[0]

for pattern in patterns:
    email = pattern.format(first=first, last=last, f=f, l=l)
    print(f"{email}@{domain}")
