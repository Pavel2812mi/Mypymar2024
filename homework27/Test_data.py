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


def generate_user_phone_number():
    """generates phone number in correct format"""
    msisdn = fake.msisdn()
    formatted_phone_number = '+' + msisdn
    return formatted_phone_number


phone_number = generate_user_phone_number()


def generate_user_address(min_length=10):
    """generates address in correct format"""
    generated_address = fake.address()
    while len(generated_address) < min_length:
        generated_address = f"{generated_address}, {fake.city()}"
    return generated_address


address = generate_user_address(10)


def generate_user_role():
    """generates user role"""
    roles = ["user", "admin", "moderator"]
    return random.choice(roles)


role = generate_user_role()


def generate_referral_code(chars="ABCDEFGH"):
    """generates referral code"""
    char_list = list(chars)
    random.shuffle(char_list)
    return "".join(char_list)


referralCode = generate_referral_code()
