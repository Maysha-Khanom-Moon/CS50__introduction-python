# real number
x = float(input("x: "))
y = float(input("y: "))

print(f"x/y: {x/y}")
# round automatically
print(f"x/y(with specific precision): {x/y:.2f}")

# us style to count number
z = 1000000000
print(f"us style to count number, z: {z:,}")


# round: nearest integer
z = 3.14159278
print(round(z))
print(round(z, 4))

# using precision, by dafualt use round
print(f"{z:.2f}")

# us style: no round and count all the digits
print(f"z={z:,}")