import requests

# URL to which the request will be sent
url = "https://hmcl-funapp-openai-ci-01t.azurewebsites.net/hero-echo-genai-mvp1/test-post"

# URL parameters
params = {
    "target": "test_snowflake_H3267dnDw3NuybXdto2"
}

# Body of the request
body = {
    "config": {
        "user": "your_username",
        "password": "your_password",
        "account": "your_account",
        "warehouse": "your_warehouse",
        "database": "your_database",
        "schema": "your_schema"
    },
    "sql": "some sql query"
}

# Make the POST request
response = requests.post(url, params=params, json=body)

# Check if the request was successful
if response.status_code == 200:
    print("Request successful!")
    print("Response:", response.json())
else:
    print("Request failed with status code:", response.status_code)
    print("Response:", response.text)
