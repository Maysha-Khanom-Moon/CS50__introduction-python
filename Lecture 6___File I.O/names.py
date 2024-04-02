names = []

for _ in range(3):
    names.append(input("What's your name? "))


for name in sorted(names):
    print(f"hello, {name}")
    

# to remove the pain of reinput the values again and again
# There the way coming file I/O to reserve these

# here we use open function