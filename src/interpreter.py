# © fifly.org 2023-present. All rights reserved.
# You may use this code in accordance with the license distributed with this code.

# If the license distributed with this code was not the FiFly Redistributable Software License version 1.0
# then this copy of this code has been distributed illegally.

# If the license was not distributed with this code you can find it at https://fifly.org/FRSL/1.0.


import os
from utils import throw_error, get_request

vars = {}
imports = []

# Gets a variable's value
def get_var_value(var_name: str):
    try:
        return vars[var_name]
    except:
        throw_error("VariableError: Variable " + var_name + " does not exist.")

# Sets a variable's value, creating one if it doesn't exist
def set_var_value(var_name: str, var_value: str):
    try:
        vars[var_name] = var_value
    except:
        throw_error("VariableError: Could not set value of " + var_name)
    
def parseArg(arg: str):
    if arg.startswith("$"):
        return get_var_value(arg[1:])
    
    arg = arg.replace(":", " ")
    arg = arg.replace("\\n", "\n")

    if arg.startswith("&input-"):
        return input(arg[7:])
    else:
        return arg

def interpret(code: str):
    codelines = code.split("\n")
    for line in codelines:
        line = line.strip()

        if line.startswith("//") or line == "":
            continue

        tokens = line.split()
        
        if tokens[0] == "print":
            print(parseArg(tokens[1]))
        elif tokens[0] == "set":
            set_var_value(tokens[1], parseArg(tokens[2]))
        elif tokens[0] == "#read_file":
            if imports.count("filesystem") == 0:
                throw_error("You cannot use file operation without importing the 'filesystem' module.")
                
            set_var_value(tokens[2], open(parseArg(tokens[1]), "r").read())
        elif tokens[0] == "#write_file":
            if imports.count("filesystem") == 0:
                throw_error("You cannot use file operation without importing the 'filesystem' module.")
                
            open(parseArg(tokens[1]), "w").write(parseArg(tokens[2]))
        elif tokens[0] == "#delete_file":
            if imports.count("filesystem") == 0:
                throw_error("You cannot use file operation without importing the 'filesystem' module.")
                
            if os.path.exists(tokens[1]):
                    os.remove(parseArg(tokens[1]))
            else:
                throw_error("File " + tokens[1] + " does not exist.")
        elif tokens[0] == "import":
            imports.append(parseArg(tokens[1]))
        elif tokens[0] == "#http_get":
            if imports.count("http") == 0:
                throw_error("You cannot use HTTP requests without importing the 'http' module.")
            
            set_var_value(tokens[2], get_request(parseArg(tokens[1])))
        elif tokens[0] == "exec":
            interpret(parseArg(tokens[1]))
        else:
            throw_error("Unexpected keyword \"" + tokens[0] + "\".")