import re
# import streamlit as st

# Define a function to extract placeholders from the template
def extract_placeholders(template):
    return re.findall(r'\[(.*?)\]', template)

# Define a function to ask questions and collect user responses
def get_user_input(question, validation_pattern=None):
    while True:
        user_input = input(question + ' ').strip()
        if validation_pattern is None or re.match(validation_pattern, user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

# Template
template = """
This Service Agreement (hereinafter referred to as the "Agreement") is entered into on [Effective Date], by and between [Service Provider], with an address of [Service Provider Address], (hereinafter referred to as the "Service Provider") and [Client], with an address of [Client Address], (hereinafter referred to as the "Client") (collectively referred to as the "Parties").

SERVICES
During the period of this Agreement, the Service Provider shall perform and provide the following services (hereinafter referred to as "Services"):
1. [_Service 1] 

PAYMENT TERMS
The Services are to be paid for as follows:
Amount at signing of this Agreement: [Amount]

This Agreement outlines the terms and conditions of the partnership between the Service Provider and the Client for the provision of the Services outlined above.
"""
def fillin(template):
    # Extract placeholders from the template
    placeholders = extract_placeholders(template)
    print(placeholders)
    # Initialize an empty dictionary to store user responses
    user_responses = {}

    # Initialize a set to keep track of placeholders that have been asked
    asked_placeholders = set()
    
    # Chatbot interaction to fill the form based on extracted placeholders
    print("Welcome to the Form-Filling Chatbot!")

    for placeholder in placeholders:
        # Check if this placeholder has already been asked
        if placeholder in asked_placeholders:
            # If yes, use the previous response
            user_responses[placeholder] = user_responses.get(placeholder, "")
            continue

        # Determine a suitable question based on the placeholder
        question = f"Please enter the details for '{placeholder}':"
        user_responses[placeholder] = get_user_input(question)

        # Mark this placeholder as asked
        asked_placeholders.add(placeholder)
    print(user_responses)
    # Fill in the template with user responses
    filled_template = template
    for placeholder, response in user_responses.items():
        filled_template = filled_template.replace(f"[{placeholder}]", response)

    # Display the filled template
    print("\nThank you! Here is the filled template:\n\n")
    print(filled_template)
    return filled_template

