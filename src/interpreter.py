# © fifly.org 2023-present. All rights reserved.
# You may use this code in accordance with the license distributed with this code.

# If the license distributed with this code was not the FiFly Redistributable Software License version 1.0
# then this copy of this code has been distributed illegally.

# If the license was not distributed with this code you can find it at https://fifly.org/FRSL/1.0.


vars = {}

def throw_error(error_message: str):
    print(error_message)
    exit(1)
    
def get_var_value(var_name: str):
    try:
        return vars[var_name]
    except:
        throw_error("VariableError: Variable " + var_name + " does not exist.")

def set_var_value(var_name: str, var_value: str):
    try:
        vars[var_name] = var_value
    except:
        throw_error("VariableError: Could not set value of " + var_name)

def interpret(code: str):
    codelines = code.split("\n")
    for line in codelines:
        line = line.strip()

        if line.startswith("//"):
            continue

        tokens = line.split()
        
        if tokens[0] == "print":
            if tokens[1].startswith("$"):
                print(get_var_value(tokens[1][1:]))
            else:
                print(tokens[1].replace("\\", " "))
        elif tokens[0] == "set":
            if tokens[2].startswith("$"):
                set_var_value(tokens[1], get_var_value(tokens[1][1:]))
            else:
                set_var_value(tokens[1], tokens[2].replace("\\", " "))
        elif tokens[0] == "#read":
            if tokens[1].startswith("$"):
                set_var_value(tokens[2], open(get_var_value(tokens[1][1:]), "r").read())
            else:
                set_var_value(tokens[2], open(tokens[1].replace("\\", " "), "r").read())
        elif tokens[0] == "#write":
            if tokens[1].startswith("$"):
                if tokens[2].startswith("$"):
                    set_var_value(tokens[2], open(get_var_value(tokens[1][1:]), "w").write(get_var_value(tokens[2][1:])))
                else:
                    set_var_value(tokens[2], open(get_var_value(tokens[1][1:]), "w").write(tokens[2]))
            else:
                if tokens[2].startswith("$"):
                    set_var_value(tokens[2], open(tokens[1], "w").write(get_var_value(tokens[2][1:])))
                else:
                    set_var_value(tokens[2], open(tokens[1], "w").write(tokens[2]))
        else:
            throw_error("Unexpected keyword \"" + tokens[0] + "\".")