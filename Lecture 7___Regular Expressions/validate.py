'''
Regular expressions are patterns used to match character combinations in strings
'''

# strip: used to remove extra whitespaces 
# or specified characters from the start and from the end

# maysha412@.com
email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and domain.endswith(".com"):
    print("Valid")
else:
    print("Invalid")

    
# if "@" in email and "." in email:

# via condition to check string format is tough