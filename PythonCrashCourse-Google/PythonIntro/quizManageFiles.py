# Question 1
# The create_python_script function creates a new python script in the current working directory, 
# adds the line of comments to it declared by the 'comments' variable, and returns the size of the new file. 
# Fill in the gaps to create a script called "program.py".

import os
import datetime

if os.path.isdir("Python Programs") == False:
    os.mkdir("Python Programs")

os.chdir("Python Programs")
print(os.getcwd())
relative = os.path.join("..", os.getcwd())
parent = os.path.abspath("..")
print(parent)

with open("program.py", "r") as file:
    pass

stamp = datetime.datetime.now()
dateportion = stamp.strftime("%Y-%m-%d")
print(dateportion)
print(stamp)
print(os.listdir())

'''
def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, "w") as file:
        file.write(comments)
        
    filesize = os.stat(filename).st_size
    return(filesize)

print(create_python_script("program.py"))
'''