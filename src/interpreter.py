# © fifly.org 2023-present. All rights reserved.
# You may use this code in accordance with the license distributed with this code.

# If the license distributed with this code was not the FiFly Redistributable Software License version 1.0
# then this copy of this code has been distributed illegally.

# If the license was not distributed with this code you can find it at https://fifly.org/FRSL/1.0.


import os
import requests

vars = {}
imports = []

# Throws an error
def throw_error(error_message: str):
    print(error_message)
    exit(1)

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

# Preforms a GET request
def get_request(url: str):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Return the content of the response
            return response.text
        else:
            # If the request was not successful, raise an exception
            response.raise_for_status()
    except Exception as e:
        # Handle exceptions (e.g., request errors, network errors)
        return f"An error occurred: {e}"
    
def parseArg(arg: str):
    if arg.startswith("$"):
        return get_var_value(arg[1:])
    
    arg = arg.replace("\\", " ")

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
        else:
            throw_error("Unexpected keyword \"" + tokens[0] + "\".")