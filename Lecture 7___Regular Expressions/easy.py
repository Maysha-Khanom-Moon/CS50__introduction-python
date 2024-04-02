# 're' library: define the format of string
import re

email = input("What's your email? ").strip()

# re.search(pattern, string, flags=0)
# if re.search("@", email):


# "\." means literily I want to match . not any other character
# and \ told me don't treat next element specially just treat as a '.' char


# do .+ not +.


# if re.search(".+@.+\.com", email):


# r means raw string


# com$ means com is the end point
# and com can be occurs only one time


# r"^[^@]+@[^@]+\.com$"
# there are 4 part:
# 1. ^[^@]+ means start from that point and except @ and must have to occurrs one or more times before @
# 2. @ match the with the @ and occurrs only one time
# 3. [^@]+ means after @ must have to occurrs other char except @
# 4. \.com$ means ending will be .com and that will occurrs only one time


# re.search(pattern, str, flag)
# if re.search(r"^[^@]+@[^@]+\.com$", email):


# \w means any word character: alphanumeric character and _
# [a-zA-Z0-9_]: \w


# never use unnecessay ' ' inside the r""


# if re.search(r"^\w+@\w+\.(com|edu|yahoo)$", str, re.IGNORECASE):
    
# if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|yahoo)$", email, re.IGNORECASE):
    
if re.search(r"^\w+@(\w+\.)*\w+\.(com|edu|yahoo)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
    


"""
.       -->  matches any character except newline
*       -->  zero or more occurrences
+       -->  one or more occurrences
?       -->  matches zero or one occurence
{m}     -->  m repetitions must
{m, n}  -->  m-n repetitions must


^       -->  matches the start of the string
$       -->  matches the end of the string just before the newline at the end of the string


[]      -->  set of characters
[^]     -->  complementing(except) the set
[a-z]   -->  a to z set of characters


\d      -->  decimal digit
\D      -->  not a decimal digit
\s      -->  whitespace characters
\S      -->  not a whitespace character
\w      -->  word character ... as well as numbers and the underscore
\W      -->  not a word character


A|B     -->  either A or B
(...)   -->  a group
(?:...) -->  non-capturing version


flags:
re.IGNORECASE
re.MULTILINE
re.DOTALL

"""