import requests

# Throws an error
def throw_error(error_message: str):
    print(error_message)
    exit(1)

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
    
def is_number(string: str):
    try:
        float(string)
        return True
    except ValueError:
        return False