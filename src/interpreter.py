# © fifly.org 2023-present. All rights reserved.
# You may use this code in accordance with the license distributed with this code.

# If the license distributed with this code was not the FiFly Redistributable Software License version 1.0
# then this copy of this code has been distributed illegally.

# If the license was not distributed with this code you can find it at https://fifly.org/FRSL/1.0.


import os
from utils import throw_error, get_request, is_number

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

    if (arg.startswith('"') and arg.endswith('"')) or (
        arg.startswith("'") and arg.endswith("'")
    ):
        return arg[1:-1]
    
    if arg.startswith("&input-"):
        return input(arg[7:])

    if is_number(arg):
        return arg
    else:
        throw_error("StringError: String must be enclosed in quotes or double quotes.")


def interpret(code: str):
    codelines = code.split("\n")
    for line in codelines:
        line = line.strip()

        if line.startswith("//") or line == "":
            continue

        tokens = line.split(None, 1)  # Split the line into tokens, max 1 split
        _tokens = line.split()
        command = _tokens[0]
        args = parseArg(tokens[1]) if len(tokens) > 1 else ""  # Parse the arguments

        if command == "print":
            print(parseArg(args))
        elif command == "set":
            set_var_value(_tokens[1], parseArg(" ".join(args.split()[1:])))
        elif command == "read_file":
            if imports.count("filesystem") == 0:
                throw_error(
                    "You cannot use file operation without importing the 'filesystem' module."
                )

            set_var_value(_tokens[2], open(parseArg(_tokens[1]), "r").read())
        elif command == "write_file":
            if imports.count("filesystem") == 0:
                throw_error(
                    "You cannot use file operation without importing the 'filesystem' module."
                )

            open(parseArg(_tokens[1]), "w").write(parseArg(_tokens[2]))
        elif command == "delete_file":
            if imports.count("filesystem") == 0:
                throw_error(
                    "You cannot use file operation without importing the 'filesystem' module."
                )

            if os.path.exists(_tokens[1]):
                os.remove(parseArg(_tokens[1]))
            else:
                throw_error("File " + _tokens[1] + " does not exist.")
        elif command == "import":
            imports.append(parseArg(_tokens[1]))
        elif command == "http_get":
            if imports.count("http") == 0:
                throw_error(
                    "You cannot use HTTP requests without importing the 'http' module."
                )

            set_var_value(_tokens[2], get_request(parseArg(_tokens[1])))
        elif command == "exec":
            interpret(parseArg(tokens[1]))
        else:
            throw_error('Unexpected keyword "' + command + '".')
