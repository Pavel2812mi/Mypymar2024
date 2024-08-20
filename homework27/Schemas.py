"""
This module contains JSON schemas
used for validating API responses.
"""


get_all_users_schema = {
    "type": "object",
    "properties": {
        "users": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "_id": {"type": "string"},
                    "name": {"type": "string"},
                    "email": {"type": "string"},
                    "createdAt": {"type": "string"},
                    "createdBy": {"type": ["integer", "string"]}
                },
                "required": ["_id", "name", "email",
                             "createdAt", "createdBy"]
            }
        },
        "totalPages": {"type": "integer"}
    },
    "required": ["users", "totalPages"]
}


get_user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "age": {"type": "integer"},
        "phoneNumber": {"type": "string"},
        "address": {"type": "string"},
        "role": {"type": "string"},
        "referralCode": {"type": "string"},
        "createdAt": {"type": "string"},
        "createdBy": {"type": "string"}
    },
    "required": ["id", "name", "email", "age", "phoneNumber",
                 "address", "role", "referralCode", "createdAt",
                 "createdBy"]
}


user_data_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "age": {"type": "integer"},
        "phoneNumber": {"type": "string"},
        "address": {"type": "string"},
        "role": {"type": "string"},
        "referralCode": {"type": "string"},
        "status": {"type": "string"}
    },
    "required": ["id", "name", "email", "age",
                 "phoneNumber", "address", "role",
                 "referralCode", "status"]
}
