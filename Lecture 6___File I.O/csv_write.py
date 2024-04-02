import csv

name = input("What's your name?")
home = input("What's your home?")

# 1. as list
# with open("csv_write.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home]) 



# 2. as dict
with open("csv_write2.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home}) 
    
# as i pass the field name so the inserting position of columns doesn't matter
  
# fieldnames(cols) have to insert before appends the values