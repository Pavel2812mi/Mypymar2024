"""Module containing shared constants and data for testing."""
import random

# Base URL of the web application
URL = "https://poker.evenbetpoker.com/html5"

# User credentials for sign up
random_number = random.randint(100000, 999999)
u_email = f"vamav{random_number}@nastyx.com"
u_nickname = f"john{random_number}"
u_password = f"poker{random_number}"
u_confirm_password = u_password


