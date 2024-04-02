name = input("whats your name: ")

# match: like switch
# match: not or, use '|'
match name:
  case "Harry" | "Hermione" | "Ron":
    print("Gryffindor")
  
  case "Draco":
    print("Slytherin")

  # default
  case _:
    print("who?")