#!/usr/bin/env python3

import base64
from datetime import datetime
import hashlib

class API:
    def __init__(self, default_expiry_days: int = 30):
        """
        Initializes the API class with a default expiry period for the tokens.
        
        :param default_expiry_days: The default number of days before the token expires.
        """
        self.default_expiry_days = default_expiry_days

    @staticmethod
    def _generate_sha256(username: str, password: str) -> str:
        """
        Generates a SHA-256 hash from the given username and password.
        :param username: The username
        :param password: The password
        """
        credentials = f"{username}:{password}"
        return hashlib.sha256(credentials.encode()).hexdigest()

    def _encode_string(self, data: str, days: int = None) -> str:
        """
        Encodes the given data with an expiry timestamp.
        
        :param data: The data to encode.
        :param days: The number of days until the data expires. Uses the default if None.
        :return: The base64-encoded string with expiry information.
        """
        if days is None:
            days = self.default_expiry_days
        
        current_timestamp = int(datetime.now().timestamp())
        expiry_timestamp = (days * 86400) + current_timestamp
        combined_data = f"{data}|{expiry_timestamp}"
        encoded_value = base64.b64encode(combined_data.encode()).decode()
        return encoded_value

    @staticmethod
    def _decode_string(encoded_data: str) -> str:
        """
        Decodes the given base64-encoded string.
        
        :param encoded_data: The base64-encoded data.
        :return: The decoded string.
        """
        decoded_data = base64.b64decode(encoded_data.encode()).decode()
        return decoded_data

    def generate_api_token(self, username: str, password: str, days: int = None) -> str:
        """
        Generates an API token for the given username and password.
        
        :param username: The username.
        :param password: The password.
        :param days: The number of days until the token expires. Uses the default if None.
        :return: The generated API token.
        """
        hash_value = self._generate_sha256(username, password)
        api_token = self._encode_string(hash_value, days)
        return api_token

    def validate_api_token(self, api_token: str):
        """
        Validates the given API token and returns the expiry time if valid.
        
        :param api_token: The API token to validate.
        :return: The expiry time if the token is valid, or None if expired.
        """
        decoded = self._decode_string(api_token)
        hash_value, expiry_time = decoded.split('|')
        expiry_time = int(expiry_time)
        current_time = int(datetime.now().timestamp())

        if expiry_time > current_time:
            return datetime.fromtimestamp(expiry_time)
        else:
            print("API key has expired.")
            return None


if __name__ == "__main__":
    api = API(default_expiry_days=30)  # You can set a different default expiry here if needed.
    username = "ganesan"
    password = "test"

    api_key = api.generate_api_token(username, password)
    print("Generated API Token:", api_key)

    validation_result = api.validate_api_token(api_key)
    print("Validation Result:", validation_result)
