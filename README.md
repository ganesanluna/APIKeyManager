# API Token Generation and Validation
This project provides a simple Python library for generating and validating API tokens with expiration dates. 
It uses SHA-256 hashing, base64 encoding, and datetime for expiry management.

## Features
- Generate API tokens with a SHA-256 hash.
- Encode tokens with an expiration date.
- Validate API tokens and check their expiry status.
- Default expiry duration can be customized.

## Requirements
- Python 3.x
- hashlib module
- base64 module
- datetime module

## Installation
Clone the repository to your local machine:

```sh
git clone https://github.com/ganesanluna/APIKeyManager.git
```

## Running the code
``` sh
cd APIKeyManager
python3 API.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.


## Example Output
```
Generated API Token: <your_encoded_api_token>
Validation Result: 2024-06-20 12:34:56
```

## Customization
You can customize the default expiry days by passing a different value to the API class constructor

``` python
api = API(default_expiry_days=50)  # Sets the default expiry to 50 days.
username = "ganesan"
password = "test"

api_key = api.generate_api_token(username, password)
print("Generated API Token:", api_key)

validation_result = api.validate_api_token(api_key)
print("Validation Result:", validation_result)
```
