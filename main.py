import requests
from bs4 import BeautifulSoup
import json
import os

# Create a session to maintain cookies and session data
session = requests.Session()

# Hardcoded file path to the JSON file containing user details
USER_DETAILS_FILE_PATH = 'user_details.json'  # Change this path if needed

# Function to extract hidden form fields (e.g., CSRF tokens)
def get_form_data(url):
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find any hidden inputs (like CSRF token) that are required for the form submission
    form_data = {}
    for input_tag in soup.find_all('input'):
        if input_tag.get('name'):
            form_data[input_tag['name']] = input_tag.get('value', '')

    return form_data

# Register a new user
def register(register_url, user_details):
    form_data = get_form_data(register_url)
    
    # Add the user details to the form data
    form_data['first_name'] = user_details['first_name']
    form_data['last_name'] = user_details['last_name']
    form_data['email'] = user_details['email']
    form_data['username'] = user_details['username']
    form_data['password'] = user_details['password']
    form_data['dob'] = user_details['dob']

    # Submit the registration form via a POST request
    response = session.post(register_url, data=form_data)
    if response.status_code == 200:
        print(f"Registration successful for {user_details['username']}.")
    else:
        print(f"Registration failed for {user_details['username']}.")
        print(response.text)

# Login to an existing account
def login(login_url, username, password):
    form_data = get_form_data(login_url)
    
    # Add login credentials to the form data
    form_data['username'] = username
    form_data['password'] = password

    # Submit the login form via a POST request
    response = session.post(login_url, data=form_data)
    if response.status_code == 200 and "Dashboard" in response.text:  # Check for a successful login
        print(f"Login successful for {username}.")
    else:
        print(f"Login failed for {username}.")
        print(response.text)

# Function to read user details from JSON file
def read_user_details():
    if not os.path.exists(USER_DETAILS_FILE_PATH):
        print(f"Error: The file '{USER_DETAILS_FILE_PATH}' does not exist.")
        return []
    
    try:
        with open(USER_DETAILS_FILE_PATH, 'r') as file:
            users = json.load(file)
            return users
    except json.JSONDecodeError:
        print(f"Error: The file content in '{USER_DETAILS_FILE_PATH}' is not a valid JSON format.")
        return []

# Main function to handle user input and registration/login
def main():
    # Ask user for the URL (same URL for both registration and login)
    url = input("Enter the URL for both registration and login: ")

    # Read user details from the hardcoded JSON file
    users = read_user_details()

    if not users:
        print("No user details found. Exiting.")
        return

    # Register each user and login
    for user in users:
        print(f"Processing {user['username']}...")
        register(url, user)
        login(url, user['username'], user['password'])

# Run the script
if __name__ == "__main__":
    main()
