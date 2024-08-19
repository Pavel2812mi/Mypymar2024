"""
This module contains the basic URL API and functions
for working with authorization.
"""


base_url = "https://alexqa.netlify.app/.netlify"

auth_token = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
              "eyJ1c2VySWQiOiIxMDM4MDAyNDI0NDQxOTEzODAwNT"
              "ciLCJpYXQiOjE3MjQwNzMwNDYsIm"
              "V4cCI6MTcyNDA3NjY0Nn0.UbY8Q0pPBitg6x"
              "L8UBKr1pePJTm7E12enuZHjtcawUk")


def get_auth_headers():
    """
    Returns authorization headers for API requests.

    Returns:
    dict: A dictionary of headers containing the authorization token
    and the JSON content type.
    """
    return {"Authorization": f"Bearer {auth_token}",
            "Content-Type": "application/json"}
