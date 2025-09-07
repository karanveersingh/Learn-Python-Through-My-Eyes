import os

# Accessing an environment variable
api_key = os.environ.get("MY_API_KEY")
if api_key:
    print(f"API Key: {api_key}")
else:
    print("MY_API_KEY environment variable not set.")

# Setting an environment variable (for the current process)
os.environ["TEMP_VAR"] = "temporary_value"
print(f"TEMP_VAR: {os.environ.get('TEMP_VAR')}")