# © fifly.org 2023-present. All rights reserved.
# You may use this code in accordance with the license distributed with this code.

# If the license distributed with this code was not the FiFly Redistributable Software License version 1.0
# then this copy of this code has been distributed illegally.

# If the license was not distributed with this code you can find it at https://fifly.org/FRSL/1.0.


import interpreter
import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument("-f", "--file", help="Filepath to Spark file (.spk)")

args = argParser.parse_args()

filepath = args.file
code = open(filepath, "r").read()

interpreter.interpret(code)