# © fifly.org 2023-present. All rights reserved.
# You may use this code in accordance with the license distributed with this code.

# If the license distributed with this code was not the FiFly Redistributable Software License version 1.0
# then this copy of this code has been distributed illegally.

# If the license was not distributed with this code you can find it at https://fifly.org/FRSL/1.0.


import interpreter
import sys
from utils import throw_error

argv = sys.argv

if argv[0].endswith("main.py"):
    filepath = argv[1]
else:
    filepath = argv[0]

code = open(filepath, "r").read()

try:
    interpreter.interpret(code)
except Exception as e:
    throw_error("Exception: " + e.__str__())