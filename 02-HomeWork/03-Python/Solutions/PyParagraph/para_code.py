import os
import re
import string
filepath = os.path.join("raw_data", "paragraph_2.txt")
paragraph=""
lines = []  
# maxitems = 0
with open(filepath, "r") as paragraphtxt:
    paragraph = paragraphtxt.read()
for line in paragraph:
    print(line)
    lines.append(line.rstrip('\n'))

