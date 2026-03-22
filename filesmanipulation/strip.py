filename = 'filesmanipulation\poem.txt'

with open(filename) as poem:
    first = poem.readline().rstrip()

print(first)   

chars = "Nam"
# no_no = first.strip(chars)
# print(no_no)

for char in first:
    if char in chars:
        print(f'removing {char}')
    else:
        break
print('*' * 20)

for char in first[::-1]:
    if char in chars:
        print(f'removing {char}')
    else:
        break

nam_removed = first.removeprefix("Nam")
print(nam_removed)
działo_removed = first.removesuffix("dziaĹ‚o")
print(działo_removed)