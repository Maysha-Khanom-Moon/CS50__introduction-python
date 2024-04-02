# pip install cowsay
# cowsay is a 3rd party python package
import cowsay

import sys

if len(sys.argv) == 2:
    # python say.py David
    # cowsay.cow("hello, " + sys.argv[1]) 
    cowsay.trex("hello, " + sys.argv[1])