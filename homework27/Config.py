"""
This module contains the basic URL API and functions
for working with authorization.
"""


base_url = "https://alexqa.netlify.app/.netlify"

auth_token = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
              "eyJ1c2VySWQiOiIxMDM4MDAyNDI0NDQx"
              "OTEzODAwNTciLCJpYXQiOjE3MjQwMTQ3M"
              "TYsImV4cCI6MTcyNDAxODMxNn0."
              "a_b3kekatx2ijQR_0YM58fi3x8Q-npBfH3HcUYgeKtk")


def get_auth_headers():
    """
    Returns authorization headers for API requests.

    Returns:
    dict: A dictionary of headers containing the authorization token
    and the JSON content type.
    """
    return {"Authorization": f"Bearer {auth_token}",
            "Content-Type": "application/json"}
