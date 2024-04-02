# for if-else: and or

score = int(input("Score: "))

if score >= 90 and score <= 100:
  print("Grade: A")

# another way for and operation
elif 80 <= score < 90:
  print("Grade: B")

elif score >= 70:
  print("Grade: C")

elif score >= 60:
  print("Grade: D")

else:
  print("Grade: F")


if score % 2:
  print("Odd")

else:
  print("Even")