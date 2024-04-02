# 1.
names = []

with open("with.txt") as file:
    for line in file:
        names.append(line.rstrip())


for name in sorted(names):
    print(f"hello, {name}")



# 2.
with open("with.txt") as file:
    for line in sorted(file, reverse=True):
        print("hello,", line.strip())


# reverse=True: sorted by descending order