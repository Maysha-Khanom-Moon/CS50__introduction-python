import re

url = input("URL: ").strip()


# replace("before", "after")
# username = url.replace("https://twitter.com/", "")


# removeprefix("remains after that")
# username = url.removeprefix("https://twitter.com/")


# re.sub(pattern, replacement, str)
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)


# re.search(pattern, str, flag=0)
matches = re.search(r"^(https?://)?(www\.)?twitter\.com/(\w+)$", url, re.IGNORECASE)
if matches:
    print(f"Username: {matches.group(3)}")
    
    


# more function
# re.split(pattern, str, maxsplit=0, flags=0)
# re.findall(pattern, str, flags=0)