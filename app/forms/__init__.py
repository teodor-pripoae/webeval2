import os
import re

python_file_exp = re.compile(r'^(\w+)\.py$')

dir_path = os.path.dirname(__file__)
file_list = os.listdir(dir_path)

#imports everything from other .py files in the directory
for f in file_list:
    match = python_file_exp.match(f)
    if match and f != os.path.basename(__file__):
        exec_string = "from "+ match.groups()[0] +" import *"
        exec exec_string
        