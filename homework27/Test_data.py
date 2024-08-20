"""
This module provides functions for generating test data
for use in API requests.
"""


# -*- coding: utf-8 -*-
import random
from faker import Faker

fake = Faker()

name = fake.name()
email = fake.email()
age = fake.random_int(min=18, max=99)
phone_number = '+' + fake.msisdn()
role = random.choice(["user", "admin", "moderator"])

symbols = "ABCDEFGH"
referralCode = ''.join(random.sample(symbols, len(symbols)))


def generate_user_address(min_length=10):
    """generates address in correct format"""
    generated_address = fake.address()
    while len(generated_address) < min_length:
        generated_address = f"{generated_address}, {fake.city()}"
    return generated_address
