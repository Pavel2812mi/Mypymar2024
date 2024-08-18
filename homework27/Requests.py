"""Module containing test cases for user management API operations."""


import logging
import requests
import jsonschema
from homework27 import Schemas, Config, API_logger_config, Test_data

logger = (API_logger_config.setup_logging
          ("API_test.log", log_level=logging.INFO))


def get_all_users():
    """
    Gets a list of all users and validates the JSON schema of the response.

    Returns:
        None: This function validates the fetched users data
         structure against a defined JSON schema.

    Raises:
        AssertionError: If the response status code is not 200,
                         or if the JSON schema of the response is invalid.
    """
    logger.info("Starting a test: Get all users and validate JSON schema")
    response = requests.get(f"{Config.base_url}/functions/getUsers",
                            headers=Config.get_auth_headers(), timeout=5)
    assert response.status_code == 200, \
        logger.error(f"Data access error:"
                     f" {response.status_code}"
                     f" {response.text}")

    try:
        jsonschema.validate(instance=response.json(),
                            schema=Schemas.get_all_users_schema)
        logger.info("The JSON schema is correct")
    except jsonschema.exceptions.ValidationError as e:
        logger.error(f"JSON schema validation error: {e}")
        raise AssertionError(e) from e
    logger.info("Get all users and validate JSON schema test"
                " successfully completed")


def create_user():
    """
    Creates a user using the API.

    Returns:
        str: ID of the created user.

    Raises:
        AssertionError: If the response status code is not 200,
                         or if the JSON schema of the response is invalid.
    """
    logger.info("Starting a test: Create user and validate JSON schema")
    data = {
        "name": Test_data.name,
        "email": Test_data.email,
        "age": Test_data.age,
        "phoneNumber": Test_data.phone_number,
        "address": Test_data.address,
        "role": Test_data.role,
        "referralCode": Test_data.referralCode
    }
    response = requests.post(f"{Config.base_url}/functions/createUser",
                             json=data, headers=Config.get_auth_headers(),
                             timeout=5)
    assert response.status_code == 200, \
        logger.error(f"Error creating user:"
                     f" {response.status_code}{response.text}")
    try:
        jsonschema.validate(instance=response.json(),
                            schema=Schemas.user_data_schema)
        logger.info("The JSON schema is correct")
    except jsonschema.exceptions.ValidationError as e:
        logger.error(f"JSON schema validation error: {e}")
        raise AssertionError(e) from e
    logger.info("Create user and validate JSON schema test"
                " successfully completed")
    return response.json()['id']


def update_created_user(created_user_id):
    """Updates previously created user with provided data.

    Args:
        created_user_id (str): ID of the user to update.

    Returns:
        str: ID of the updated user.

    Raises:
        AssertionError: If the request fails
         or the response does not match the expected schema.
    """
    logger.info("Starting a test: Update created user"
                " and validate JSON schema")
    data = {
        "name": Test_data.name,
        "email": Test_data.email,
        "age": Test_data.age,
        "phoneNumber": Test_data.phone_number,
        "address": Test_data.address,
        "role": Test_data.role,
        "referralCode": Test_data.referralCode
    }
    response = requests.put(f"{Config.base_url}/"
                            f"functions/updateUser/{created_user_id}",
                            json=data, headers=Config.get_auth_headers(),
                            timeout=5)
    assert response.status_code == 200, \
        logger.error(f"Error updating user:"
                     f" {response.status_code}"
                     f" {response.text}")

    try:
        jsonschema.validate(instance=response.json(),
                            schema=Schemas.user_data_schema)
        logger.info("The JSON schema is correct")
    except jsonschema.exceptions.ValidationError as e:
        logger.error(f"JSON schema validation error: {e}")
        raise AssertionError(e) from e
    logger.info("Update created user and "
                "validate JSON schema test successfully completed")
    return response.json()['id']


def get_updated_user(updated_user_id):
    """
     Fetches previously updated user data from the API endpoint
     using provided authentication token and user ID.

    Args:
        updated_user_id (str): The ID of the user whose data is being fetched.

    Returns:
        None: This function validates the fetched user data structure
        against a defined JSON schema.

    Raises:
        AssertionError: If the API request fails
         or the fetched data does not conform to the defined schema.
    """
    logger.info("Starting a test: Get updated user"
                " and validate JSON schema")
    response = requests.get(f"{Config.base_url}/functions/getUser/"
                            f"{updated_user_id}",
                            headers=Config.get_auth_headers(), timeout=5)
    assert response.status_code == 200, \
        f"Data access error: {response.status_code}{response.text}"

    try:
        jsonschema.validate(instance=response.json(),
                            schema=Schemas.get_user_schema)
        logger.info("The JSON schema is correct")
    except jsonschema.exceptions.ValidationError as e:
        logger.error(f"JSON schema validation error: {e}")
        raise AssertionError(e) from e
    logger.info("Get updated user and "
                "validate JSON schema test successfully completed")


def delete_updated_user(updated_user_id):
    """
    Deletes an updated user.

    Args:
        updated_user_id (str): The ID of the updated user to delete.
    """
    logger.info("Starting a test: Delete updated user")
    response = requests.delete(f"{Config.base_url}"
                               f"/functions/deleteUser/"
                               f"{updated_user_id}",
                               headers=Config.get_auth_headers(), timeout=5)
    print(response.status_code)
    print(response.json())
    logger.info("Delete updated user test successfully completed")


def delete_nonexistent_user(nonexistent_user_id):
    """
    Deletes a nonexistent user, expecting a 404 error.

    Args:
        nonexistent_user_id (str): The ID of the nonexistent user to delete.
    """
    logger.info("Starting a test: Delete nonexistent user")
    response = requests.delete(f"{Config.base_url}/functions/deleteUser/"
                               f"{nonexistent_user_id}",
                               headers=Config.get_auth_headers(), timeout=5)
    print(response.status_code)
    print(response.json())
    logger.info("Delete nonexistent user test successfully completed")


def get_nonexistent_user(nonexistent_user_id):
    """
    Gets a nonexistent user, expecting a 404 error.

    Args:
        nonexistent_user_id (str): The ID of the nonexistent user to get.
    """
    logger.info("Starting a test: Get nonexistent user")
    response = requests.get(f"{Config.base_url}/functions/getUser/"
                            f"{nonexistent_user_id}",
                            headers=Config.get_auth_headers(), timeout=5)
    assert response.status_code == 404, \
        logger.error(f"Ошибка: ожидался код 404,"
                     f" получен {response.status_code}")
    assert "User not found" in response.text, \
        logger.error(f"Ошибка: сообщение об ошибке"
                     f" не найдено в ответе: {response.text}")
    logger.info("Get nonexistent user test successfully completed")


get_all_users()
created_user_id = create_user()
updated_user_id = update_created_user(created_user_id)
get_updated_user(updated_user_id)
delete_updated_user(updated_user_id)
delete_nonexistent_user("56a6d33ec94000a7c15d17d7")
get_nonexistent_user("56a6d33ec94000a7c15d17d7")
